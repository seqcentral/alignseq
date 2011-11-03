#!/opt/local/bin/python2.7

'''
## Expected UX commands (subject to change b/c how to represent array for dataset files?)
execute
	seqcentral blast ...
	seqcentral bwa ...


list
	seqcentral list users
	seqcentral list users where id=1
	seqcentral list datasets
	seqcentral list datasets/1/sequences

get
	seqcentral get users/1
	seqcentral get collaborations/2

update
	seqcentral update collaborations/3

add
	seqcentral add datasets/1/users/3

remove
	seqcentral remove datasets/1/users/4

delete
	seqcentral delete datasets/1


Resource
	list	GET /resource 			seqcentral list collaborations|datasets|executables|hits|jobs|sequences|users
	create	POST /resource 			seqcentral create collaboration|dataset|executable|hit|job|sequence|user
	get 	GET /resource/{id} 		seqcentral get collaboration|dataset|executable|hit|job|sequence|user/{id}
	update	POST /resource/{id} 	seqcentral update collaboration|dataset|executable|hit|job|sequence|user/{id}
	delete	DELETE /resource/{id}	seqcentral delete collaboration|dataset|executable|hit|job|sequence|user/{id}

Subresource
	list	GET /resource/{id}/subresource 	seqcentral list users in collaboration/1
	list	GET /resource/{id}/subresource 	seqcentral list snps in job/1
	list	GET /resource/{id}/subresource 	seqcentral list accesses in dataset/1

Admins/Collaborators
	add		PUT	/resource/{id}/subresource/{id}		seqcentral add user/1 to dataset/3
	remove	DELETE /resource/{id}/subresource/{id} 	seqcentral remove user/1 from dataset/3
'''

import ConfigParser
import sys
import re
import argparse
import json

# add path to alignseq.py
sys.path.append('..')
# add path to OAuthSimple.py
sys.path.append('../../oauthsimple/python/OAuthSimple')

import alignseq


config = ConfigParser.RawConfigParser()
config.read('../../alignseq.conf')

client = alignseq.AlignSeq({ 'consumer_key': config.get('oauth', 'consumer_key'), \
    'consumer_secret': config.get('oauth', 'consumer_secret')})


def valid_instance(instance):
	if re.match("(collaboration|dataset|executable|hit|job|sequence|user)/\d+", instance):
		return "s/".join(instance.split('/'));
		# return True
	else:
		return False

class ToBoolean(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		if values == 'False':
			setattr(namespace, self.dest, False)
		elif values == 'True':
			setattr(namespace, self.dest, True)

def to_python_type(type):
	if type == 'integer':
		return int
	elif type == 'number':
		return float
	else:
		return str

def parse_opts(schema, unparsed_args):
	parser = argparse.ArgumentParser(description='SPECIFIC OPTIONS.')

	if 'properties' in schema:
		for key, value in schema['properties'].iteritems():
			if value['type'] == 'boolean':
				parser.add_argument('--'+key, type=str, help=value['description'], choices=['True', 'False'], action=ToBoolean)
			elif 'enum' in value:
				parser.add_argument('--'+key, type=to_python_type(value['type']), help=value['description'], choices=value['enum'])
			else:
				parser.add_argument('--'+key, type=to_python_type(value['type']), help=value['description'])

	opt = vars(parser.parse_args(unparsed_args))
	print opt
	for key, value in opt.items():
		if (value == None):
			del opt[key]

	return opt


def get_options(resource, verb):
	json_schema = client.options(resource)['data'][verb]
	schema = json.loads(json_schema)
	return schema

def get_list(parsed_args, unparsed_args):
	schema = get_options(parsed_args.resource, 'get')
	if parsed_args.options:
		return schema

	opt = parse_opts(schema, unparsed_args)

	return client.get(parsed_args.resource, opt)


def get_resources(parsed_args, unparsed_args):
	if 'for' in unparsed_args:
		parser = argparse.ArgumentParser(description='SUBRESOURCE.')
		parser.add_argument('for', help='for')
		parser.add_argument('instance', help='instance')
		opt = parser.parse_known_args(unparsed_args)

		instance = valid_instance(opt[0].instance)
		if instance:
			parsed_args.resource = instance+'/'+parsed_args.resource
			return get_list(parsed_args, opt[1])
		else:
			return False
	else:
		return get_list(parsed_args, unparsed_args)


def get_instance(parsed_args, unparsed_args):
	instance = valid_instance(parsed_args.instance)
	if instance:
		schema = get_options(instance, 'get')
		if parsed_args.options:
			return schema

		opt = parse_opts(schema, unparsed_args)

		return client.get(instance, opt)
	else:
		return False

def create_instance(parsed_args, unparsed_args):
	schema = get_options(parsed_args.resource+'s', 'post')
	if parsed_args.options:
		return schema

	opt = parse_opts(schema, unparsed_args)

	return client.post(parsed_args.resource+'s', opt)

def update_instance(parsed_args, unparsed_args):
	instance = valid_instance(parsed_args.instance)
	if instance:
		schema = get_options(instance, 'post')
		if parsed_args.options:
			return schema

		opt = parse_opts(schema, unparsed_args)

		return client.post(instance, opt)
	else:
		return False

def delete_instance(parsed_args, unparsed_args):
	instance = valid_instance(parsed_args.instance)
	if instance:
		schema = get_options(instance, 'delete')
		if parsed_args.options:
			return schema

		opt = parse_opts(schema, unparsed_args)

		return client.delete(instance, opt)
	else:
		return False

def add_user_collab(parsed_args, unparsed_args):
	user_collab = valid_instance(parsed_args.user_collab)
	instance = valid_instance(parsed_args.instance)
	if instance and user_collab:
		schema = get_options(instance+'/'+user_collab, 'put')
		if parsed_args.options:
			return schema

		opt = parse_opts(schema, unparsed_args)

		return client.put(instance+'/'+user_collab, opt)
	else:
		return False

def remove_user_collab(parsed_args, unparsed_args):
	user_collab = valid_instance(parsed_args.user_collab)
	instance = valid_instance(parsed_args.instance)
	if instance and user_collab:
		schema = get_options(instance+'/'+user_collab, 'delete')
		if parsed_args.options:
			return schema

		opt = parse_opts(schema, unparsed_args)

		return client.delete(instance+'/'+user_collab, opt)
	else:
		return False


parser = argparse.ArgumentParser(description='Do work with SeqCentral.')
subparsers = parser.add_subparsers(title='Subcommands',
	description='Valid subcommands',
	help='Helpful description')

help_parser = subparsers.add_parser('help', help='show options')
help_parser.add_argument('resource', help='Available resources')
help_parser.set_defaults(func=get_options)

list_parser = subparsers.add_parser('list', help='list existing instances')
list_parser.add_argument('resource', help='Available resources',
	choices=['collaborations', 'datasets', 'executables', 'hits', 'jobs', 'sequences', 'users'])
list_parser.add_argument('--options', action='store_true', default=False, help='show options')
list_parser.set_defaults(func=get_resources)

create_parser = subparsers.add_parser('create', help='create a new instance')
create_parser.add_argument('resource', help='Available resources',
	choices=['collaboration', 'dataset', 'executable', 'job', 'users'])
create_parser.add_argument('--options', action='store_true', default=False, help='show options')
create_parser.set_defaults(func=create_instance)

get_parser = subparsers.add_parser('get', help='get an existing instance')
get_parser.add_argument('instance', help='Instance to retrieve')
get_parser.add_argument('--options', action='store_true', default=False, help='show options')
get_parser.set_defaults(func=get_instance)

update_parser = subparsers.add_parser('update', help='update an existing instance')
update_parser.add_argument('instance', help='Instance to update')
update_parser.add_argument('--options', action='store_true', default=False, help='show options')
update_parser.set_defaults(func=update_instance)

delete_parser = subparsers.add_parser('delete', help='delete an existing instance')
delete_parser.add_argument('instance', help='Instance to delete')
delete_parser.add_argument('--options', action='store_true', default=False, help='show options')
delete_parser.set_defaults(func=delete_instance)

add_parser = subparsers.add_parser('add', help='add collaborators to instance')
add_parser.add_argument('user_collab', help='User/Collab to add')
add_parser.add_argument('to', help='to', choices=['to'])
add_parser.add_argument('instance', help='Instance')
add_parser.add_argument('--options', action='store_true', default=False, help='show options')
add_parser.set_defaults(func=add_user_collab)

remove_parser = subparsers.add_parser('remove', help='remove collaborators from instance')
remove_parser.add_argument('user_collab', help='User/Collab to add')
remove_parser.add_argument('from', help='from', choices=['from'])
remove_parser.add_argument('instance', help='Instance')
remove_parser.add_argument('--options', action='store_true', default=False, help='show options')
remove_parser.set_defaults(func=remove_user_collab)



args = parser.parse_known_args()
print json.dumps(args[0].func(args[0], args[1]), sort_keys=True, indent=2)
