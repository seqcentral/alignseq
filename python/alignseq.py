import alignseq_oauth
import json

class AlignSeq(object):

    NUCL_SEQ = 1
    PROT_SEQ = 2

    VERSION = '1.0-rc1'
    SERVER = 'http://api.seqcentral.com/alignseq'

    url = ''
    response = ''

    _oauth = None

    def __init__( self, params ):
        # If you wish to use your own OAuth client, make your changes here and in 'make_oauth_request()'
        if 'consumer_key' in params and 'consumer_secret' in params:
            self._oauth = alignseq_oauth.AlignSeq_OAuth(params['consumer_key'], params['consumer_secret'])
        else:
            print 'Incorrect parameters'

     # Method: make_oauth_request
     #    Make an OAuth authenticated request to the SeqCentral REST service.
     #
     # Access:
     #     Private
     #
     # Parameters:
     #    method - _string_ (Required) The HTTP request method type: 'get', 'post', 'put', or 'delete'
     #    url - _string_ (Required) The url to direct the request to.
     #    opt - _array_ (Required) An associative array of parameters whose keys depend on the URI accessed.
     #
     # Returns:
     #    Object containing parsed Response
    def __make_oauth_request( self, method, url, opt = {} ):
        self.url = url
        # If you wish to use your own OAuth client, make your changes here and in '__init__()'
        self.response = self._oauth.make_request(method, url, opt)[1]
        return json.loads(self.response)


    #
     # Method: get
     #    Generic method to send an HTTP GET request to the SeqCentral REST service.
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    uri - _string_ (Required) The location of the resource to access.
     #    opt - _array_ (Optional) An associative array of parameters whose keys depend on the URI accessed.
     #
     # Returns:
     #
     #
    def get( self, uri, opt = {} ):
        return self.__make_oauth_request('GET', '%s/%s/%s' % (self.SERVER, self.VERSION, uri), opt)

    #
     # Method: post
     #    Generic method to send an HTTP POST request to the SeqCentral REST service.
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    uri - _string_ (Required) The location of the resource to access.
     #    opt - _array_ (Optional) An associative array of parameters whose keys depend on the URI accessed.
     #
     # Returns:
     #
     #
    def post( self, uri, opt = {} ):
        return self.__make_oauth_request('POST', '%s/%s/%s' % (self.SERVER, self.VERSION, uri), opt)

    #
     # Method: put
     #    Generic method to send an HTTP PUT request to the SeqCentral REST service.
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    uri - _string_ (Required) The location of the resource to access.
     #    opt - _array_ (Optional) An associative array of parameters whose keys depend on the URI accessed.
     #
     # Returns:
     #
     #
    def put( self, uri, opt = {} ):
        return self.__make_oauth_request('PUT', '%s/%s/%s' % (self.SERVER, self.VERSION, uri), opt)

    #
     # Method: delete
     #    Generic method to send an HTTP DELETE request to the SeqCentral REST service.
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    uri - _string_ (Required) The location of the resource to access.
     #    opt - _array_ (Optional) An associative array of parameters whose keys depend on the URI accessed.
     #
     # Returns:
     #
     #
    def delete( self, uri, opt = {} ):
        return self.__make_oauth_request('DELETE', '%s/%s/%s' % (self.SERVER, self.VERSION, uri), opt)

     # Method: list_users
     #     Retrieve list of users
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     User List Response
    def list_users( self, opt = {} ):
        return self.get("users", opt)

     # Method: create_user
     #     Create new user
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    username - _string_ (Required) todo
     #    email - _string_ (Required) todo
     #    password - _string_ (Required) todo
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    keep_in_loop - _boolean_ (Optional) todo
     #
     # Returns:
     #     User Instance Response
    def create_user( self, username, email, password, opt = {} ):
        opt['username'] = username;
        opt['email'] = email;
        opt['password'] = password;
        return self.post("users", opt)

     # Method: get_user
     #     Retrieve single, specific user
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #
     # Returns:
     #     User Instance Response
    def get_user( self, user_id ):
        return self.get("users/%d" % (user_id))

     # Method: update_user
     #     Update user
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    affiliation - _string_ (Optional) todo
     #    keep_in_loop - _boolean_ (Optional) todo
     #    name - _string_ (Optional) todo
     #
     # Returns:
     #     User Instance Response
    def update_user( self, user_id, opt = {} ):
        return self.post("users/%d" % (user_id), opt)

     # Method: delete_user
     #     Delete user
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #
     # Returns:
     #     User List Response
    def delete_user( self, user_id ):
        return self.delete("users/%d" % (user_id))

     # Method: list_user_administrators
     #     Retrieve list of administrators for this user
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Administrator List Response
    def list_user_administrators( self, user_id, opt = {} ):
        return self.get("users/%d/administrators" % (user_id), opt)

     # Method: add_user_administrator
     #     Add admin to user
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def add_user_administrator( self, user_id, administrator_id ):
        return self.put("users/%d/administrators/%d" % (user_id, administrator_id))

     # Method: remove_user_administrator
     #     Remove admin from user
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def remove_user_administrator( self, user_id, administrator_id ):
        return self.delete("users/%d/administrators/%d" % (user_id, administrator_id))

     # Method: list_user_collaborations
     #     Retrieve list of collaborations this user is a member of
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Collaboration List Response
    def list_user_collaborations( self, user_id, opt = {} ):
        return self.get("users/%d/collaborations" % (user_id), opt)

     # Method: list_user_jobs
     #     Retrieve list of jobs this user has access to
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Job List Response
    def list_user_jobs( self, user_id, opt = {} ):
        return self.get("users/%d/jobs" % (user_id), opt)

     # Method: list_user_datasets
     #     Retrieve list of datasets this user has access to
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Dataset List Response
    def list_user_datasets( self, user_id, opt = {} ):
        return self.get("users/%d/datasets" % (user_id), opt)

     # Method: list_user_executables
     #     Retrieve list of executables this user has access to
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    user_id - _integer_ (Required) The ser identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Executable List Response
    def list_user_executables( self, user_id, opt = {} ):
        return self.get("users/%d/executables" % (user_id), opt)

     # Method: list_collaborations
     #     Retrieve list of collaborations
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Collaboration List Response
    def list_collaborations( self, opt = {} ):
        return self.get("collaborations", opt)

     # Method: create_collaboration
     #     Create new collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    name - _string_ (Required) Short human-readable name of collaboration.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    description - _string_ (Optional) Longer human-readable description of collaboration.
     #
     # Returns:
     #     Collaboration Instance Response
    def create_collaboration( self, name, opt = {} ):
        opt['name'] = name;
        return self.post("collaborations", opt)

     # Method: get_collaboration
     #     Retrieve single, specific collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #
     # Returns:
     #     Collaboration Instance Response
    def get_collaboration( self, collaboration_id ):
        return self.get("collaborations/%d" % (collaboration_id))

     # Method: update_collaboration
     #     Update collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    description - _string_ (Optional) Longer human-readable description of collaboration.
     #    name - _string_ (Optional) Short human-readable name of collaboration.
     #
     # Returns:
     #     Collaboration Instance Response
    def update_collaboration( self, collaboration_id, opt = {} ):
        return self.post("collaborations/%d" % (collaboration_id), opt)

     # Method: delete_collaboration
     #     Delete collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #
     # Returns:
     #     Collaboration List Response
    def delete_collaboration( self, collaboration_id ):
        return self.delete("collaborations/%d" % (collaboration_id))

     # Method: list_collaboration_administrators
     #     Retrieve list of administrators for this collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Administrator List Response
    def list_collaboration_administrators( self, collaboration_id, opt = {} ):
        return self.get("collaborations/%d/administrators" % (collaboration_id), opt)

     # Method: add_collaboration_administrator
     #     Add admin to collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def add_collaboration_administrator( self, collaboration_id, administrator_id ):
        return self.put("collaborations/%d/administrators/%d" % (collaboration_id, administrator_id))

     # Method: remove_collaboration_administrator
     #     Remove admin from collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def remove_collaboration_administrator( self, collaboration_id, administrator_id ):
        return self.delete("collaborations/%d/administrators/%d" % (collaboration_id, administrator_id))

     # Method: list_collaboration_users
     #     Retrieve list of users this collaboration has access to
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     User List Response
    def list_collaboration_users( self, collaboration_id, opt = {} ):
        return self.get("collaborations/%d/users" % (collaboration_id), opt)

     # Method: add_collaboration_user
     #     Add user to collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    user_id - _integer_ (Required) The ser identifier.
     #
     # Returns:
     #     User List Response
    def add_collaboration_user( self, collaboration_id, user_id ):
        return self.put("collaborations/%d/users/%d" % (collaboration_id, user_id))

     # Method: remove_collaboration_user
     #     Remove user from collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    user_id - _integer_ (Required) The ser identifier.
     #
     # Returns:
     #     User List Response
    def remove_collaboration_user( self, collaboration_id, user_id ):
        return self.delete("collaborations/%d/users/%d" % (collaboration_id, user_id))

     # Method: list_collaboration_jobs
     #     Retrieve list of jobs this collaboration has access to
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Job List Response
    def list_collaboration_jobs( self, collaboration_id, opt = {} ):
        return self.get("collaborations/%d/jobs" % (collaboration_id), opt)

     # Method: add_collaboration_job
     #     Add job to collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    job_id - _integer_ (Required) The ob identifier.
     #
     # Returns:
     #     Job List Response
    def add_collaboration_job( self, collaboration_id, job_id ):
        return self.put("collaborations/%d/jobs/%d" % (collaboration_id, job_id))

     # Method: remove_collaboration_job
     #     Remove job from collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    job_id - _integer_ (Required) The ob identifier.
     #
     # Returns:
     #     Job List Response
    def remove_collaboration_job( self, collaboration_id, job_id ):
        return self.delete("collaborations/%d/jobs/%d" % (collaboration_id, job_id))

     # Method: list_collaboration_datasets
     #     Retrieve list of datasets this collaboration has access to
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Dataset List Response
    def list_collaboration_datasets( self, collaboration_id, opt = {} ):
        return self.get("collaborations/%d/datasets" % (collaboration_id), opt)

     # Method: add_collaboration_dataset
     #     Add dataset to collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #
     # Returns:
     #     Dataset List Response
    def add_collaboration_dataset( self, collaboration_id, dataset_id ):
        return self.put("collaborations/%d/datasets/%d" % (collaboration_id, dataset_id))

     # Method: remove_collaboration_dataset
     #     Remove dataset from collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #
     # Returns:
     #     Dataset List Response
    def remove_collaboration_dataset( self, collaboration_id, dataset_id ):
        return self.delete("collaborations/%d/datasets/%d" % (collaboration_id, dataset_id))

     # Method: list_collaboration_executables
     #     Retrieve list of executables this collaboration has access to
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Executable List Response
    def list_collaboration_executables( self, collaboration_id, opt = {} ):
        return self.get("collaborations/%d/executables" % (collaboration_id), opt)

     # Method: add_collaboration_executable
     #     Add executable to collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #
     # Returns:
     #     Executable List Response
    def add_collaboration_executable( self, collaboration_id, executable_id ):
        return self.put("collaborations/%d/executables/%d" % (collaboration_id, executable_id))

     # Method: remove_collaboration_executable
     #     Remove executable from collaboration
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    collaboration_id - _integer_ (Required) The ollaboration identifier.
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #
     # Returns:
     #     Executable List Response
    def remove_collaboration_executable( self, collaboration_id, executable_id ):
        return self.delete("collaborations/%d/executables/%d" % (collaboration_id, executable_id))

     # Method: list_jobs
     #     Retrieve list of jobs
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Job List Response
    def list_jobs( self, opt = {} ):
        return self.get("jobs", opt)

     # Method: create_job
     #     Create new job
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    name - _string_ (Required) Short human-readable name of job
     #    executable_id - _integer_ (Required) Identifier of executable to use
     #    queries - _array_ (Required) Array of dataset ids to use as queries
     #    targets - _array_ (Required) Array of of dataset ids to use as targets
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    description - _string_ (Optional) Longer human-readable description of job
     #    executable_parameters - _array_ (Optional) Array of search parameters specific to executable
     #    notify - _boolean_ (Optional) Be notified via email when job is completed
     #
     # Returns:
     #     Job Instance Response
    def create_job( self, name, executable_id, queries, targets, opt = {} ):
        opt['name'] = name;
        opt['executable_id'] = executable_id;
        opt['queries'] = queries;
        opt['targets'] = targets;
        return self.post("jobs", opt)

     # Method: get_job
     #     Retrieve single, specific job
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #
     # Returns:
     #     Job Instance Response
    def get_job( self, job_id ):
        return self.get("jobs/%d" % (job_id))

     # Method: update_job
     #     Update job
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    description - _string_ (Optional) Longer human-readable description of job
     #    name - _string_ (Optional) Short human-readable name of job
     #    notify - _boolean_ (Optional) Be notified via email when job is completed
     #    public - _boolean_ (Optional) todo
     #
     # Returns:
     #     Job Instance Response
    def update_job( self, job_id, opt = {} ):
        return self.post("jobs/%d" % (job_id), opt)

     # Method: delete_job
     #     Delete job
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #
     # Returns:
     #     Job List Response
    def delete_job( self, job_id ):
        return self.delete("jobs/%d" % (job_id))

     # Method: list_job_administrators
     #     Retrieve list of administrators for this job
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Administrator List Response
    def list_job_administrators( self, job_id, opt = {} ):
        return self.get("jobs/%d/administrators" % (job_id), opt)

     # Method: add_job_administrator
     #     Add admin to job
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def add_job_administrator( self, job_id, administrator_id ):
        return self.put("jobs/%d/administrators/%d" % (job_id, administrator_id))

     # Method: remove_job_administrator
     #     Remove admin from job
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def remove_job_administrator( self, job_id, administrator_id ):
        return self.delete("jobs/%d/administrators/%d" % (job_id, administrator_id))

     # Method: list_job_collaborations
     #     Retrieve list of collaborations this job is part of
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Collaboration List Response
    def list_job_collaborations( self, job_id, opt = {} ):
        return self.get("jobs/%d/collaborations" % (job_id), opt)

     # Method: list_job_datasets
     #     Retrieve list of datasets this job used
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Dataset List Response
    def list_job_datasets( self, job_id, opt = {} ):
        return self.get("jobs/%d/datasets" % (job_id), opt)

     # Method: list_job_executables
     #     Retrieve list of executables this job used
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Executable List Response
    def list_job_executables( self, job_id, opt = {} ):
        return self.get("jobs/%d/executables" % (job_id), opt)

     # Method: list_job_hits
     #     Retrieve list of hits this job created
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    job_id - _integer_ (Required) The ob identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Hit List Response
    def list_job_hits( self, job_id, opt = {} ):
        return self.get("jobs/%d/hits" % (job_id), opt)

     # Method: list_datasets
     #     Retrieve list of datasets
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    datatype - _integer_ (Optional) Type of data represented by sequences in dataset: 1 = nucleotide, 2 = protein
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Dataset List Response
    def list_datasets( self, opt = {} ):
        return self.get("datasets", opt)

     # Method: create_dataset
     #     Create new dataset
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    name - _string_ (Required) Short human-readable name of dataset
     #    datatype - _integer_ (Required) Type of data represented by sequences in dataset: 1 = nucleotide, 2 = protein
     #    files - _array_ (Required) Array of 2-element arrays of source files and their MD5 signatures
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    description - _string_ (Optional) Longer human-readable description of dataset
     #    public - _boolean_ (Optional) todo
     #    source - _string_ (Optional) Source of dataset. E.g., VBI, Broad, JCVI
     #    version - _string_ (Optional) Version descriptor of the dataset
     #
     # Returns:
     #     Dataset Instance Response
    def create_dataset( self, name, datatype, files, opt = {} ):
        opt['name'] = name;
        opt['datatype'] = datatype;
        opt['files'] = files;
        return self.post("datasets", opt)

     # Method: get_dataset
     #     Retrieve single, specific dataset
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #
     # Returns:
     #     Dataset Instance Response
    def get_dataset( self, dataset_id ):
        return self.get("datasets/%d" % (dataset_id))

     # Method: update_dataset
     #     Update dataset
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    description - _string_ (Optional) Longer human-readable description of dataset
     #    name - _string_ (Optional) Short human-readable name of dataset
     #    public - _boolean_ (Optional) todo
     #
     # Returns:
     #     Dataset Instance Response
    def update_dataset( self, dataset_id, opt = {} ):
        return self.post("datasets/%d" % (dataset_id), opt)

     # Method: delete_dataset
     #     Delete dataset
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #
     # Returns:
     #     Dataset List Response
    def delete_dataset( self, dataset_id ):
        return self.delete("datasets/%d" % (dataset_id))

     # Method: list_dataset_administrators
     #     Retrieve list of administrators for this dataset
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Administrator List Response
    def list_dataset_administrators( self, dataset_id, opt = {} ):
        return self.get("datasets/%d/administrators" % (dataset_id), opt)

     # Method: add_dataset_administrator
     #     Add admin to dataset
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def add_dataset_administrator( self, dataset_id, administrator_id ):
        return self.put("datasets/%d/administrators/%d" % (dataset_id, administrator_id))

     # Method: remove_dataset_administrator
     #     Remove admin from dataset
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def remove_dataset_administrator( self, dataset_id, administrator_id ):
        return self.delete("datasets/%d/administrators/%d" % (dataset_id, administrator_id))

     # Method: list_dataset_collaborations
     #     Retrieve list of collaborations this dataset is a part of
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Collaboration List Response
    def list_dataset_collaborations( self, dataset_id, opt = {} ):
        return self.get("datasets/%d/collaborations" % (dataset_id), opt)

     # Method: list_dataset_jobs
     #     Retrieve list of jobs that used this dataset
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Job List Response
    def list_dataset_jobs( self, dataset_id, opt = {} ):
        return self.get("datasets/%d/jobs" % (dataset_id), opt)

     # Method: list_dataset_sequences
     #     Retrieve list of sequences this dataset contains
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    dataset_id - _integer_ (Required) The ataset identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Sequence List Response
    def list_dataset_sequences( self, dataset_id, opt = {} ):
        return self.get("datasets/%d/sequences" % (dataset_id), opt)

     # Method: list_executables
     #     Retrieve list of executables
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    datatype_query - _integer_ (Optional) todo
     #    datatype_target - _integer_ (Optional) todo
     #    institution - _string_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Executable List Response
    def list_executables( self, opt = {} ):
        return self.get("executables", opt)

     # Method: create_executable
     #     Create new executable
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    name - _string_ (Required) todo
     #    version - _string_ (Required) todo
     #    datatype_query - _integer_ (Required) todo
     #    datatype_target - _integer_ (Required) todo
     #    factor - _float_ (Required) todo
     #    input_parameters - _array_ (Required) todo
     #    output_parameters - _array_ (Required) todo
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    institution - _string_ (Optional) todo
     #    public - _boolean_ (Optional) todo
     #
     # Returns:
     #     Executable Instance Response
    def create_executable( self, name, version, datatype_query, datatype_target, factor, input_parameters, output_parameters, opt = {} ):
        opt['name'] = name;
        opt['version'] = version;
        opt['datatype_query'] = datatype_query;
        opt['datatype_target'] = datatype_target;
        opt['factor'] = factor;
        opt['input_parameters'] = input_parameters;
        opt['output_parameters'] = output_parameters;
        return self.post("executables", opt)

     # Method: get_executable
     #     Retrieve single, specific executable
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #
     # Returns:
     #     Executable Instance Response
    def get_executable( self, executable_id ):
        return self.get("executables/%d" % (executable_id))

     # Method: update_executable
     #     Update executable
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    description - _string_ (Optional) todo
     #    name - _string_ (Optional) todo
     #    public - _boolean_ (Optional) todo
     #
     # Returns:
     #     Executable Instance Response
    def update_executable( self, executable_id, opt = {} ):
        return self.post("executables/%d" % (executable_id), opt)

     # Method: delete_executable
     #     Delete executable
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #
     # Returns:
     #     Executable List Response
    def delete_executable( self, executable_id ):
        return self.delete("executables/%d" % (executable_id))

     # Method: list_executable_administrators
     #     Retrieve list of administrators for this executable
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Administrator List Response
    def list_executable_administrators( self, executable_id, opt = {} ):
        return self.get("executables/%d/administrators" % (executable_id), opt)

     # Method: add_executable_administrator
     #     Add admin to executable
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def add_executable_administrator( self, executable_id, administrator_id ):
        return self.put("executables/%d/administrators/%d" % (executable_id, administrator_id))

     # Method: remove_executable_administrator
     #     Remove admin from executable
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def remove_executable_administrator( self, executable_id, administrator_id ):
        return self.delete("executables/%d/administrators/%d" % (executable_id, administrator_id))

     # Method: list_executable_collaborations
     #     Retrieve list of collaborations this executable is a part of
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Collaboration List Response
    def list_executable_collaborations( self, executable_id, opt = {} ):
        return self.get("executables/%d/collaborations" % (executable_id), opt)

     # Method: list_executable_jobs
     #     Retrieve list of executables this job is a part of
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    executable_id - _integer_ (Required) The xecutable identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Job List Response
    def list_executable_jobs( self, executable_id, opt = {} ):
        return self.get("executables/%d/jobs" % (executable_id), opt)

     # Method: list_sequences
     #     Retrieve list of sequences
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Sequence List Response
    def list_sequences( self, opt = {} ):
        return self.get("sequences", opt)

     # Method: get_sequence
     #     Retrieve single, specific sequence
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    sequence_id - _integer_ (Required) The equence identifier.
     #
     # Returns:
     #     Sequence Instance Response
    def get_sequence( self, sequence_id ):
        return self.get("sequences/%d" % (sequence_id))

     # Method: update_sequence
     #     Update sequences
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    sequence_id - _integer_ (Required) The equence identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    name - _string_ (Optional) todo
     #
     # Returns:
     #     Sequence Instance Response
    def update_sequence( self, sequence_id, opt = {} ):
        return self.post("sequences/%d" % (sequence_id), opt)

     # Method: delete_sequence
     #     Delete sequence
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    sequence_id - _integer_ (Required) The equence identifier.
     #
     # Returns:
     #     Sequence List Response
    def delete_sequence( self, sequence_id ):
        return self.delete("sequences/%d" % (sequence_id))

     # Method: list_sequence_administrators
     #     Retrieve list of administrators for this sequence
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    sequence_id - _integer_ (Required) The equence identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Administrator List Response
    def list_sequence_administrators( self, sequence_id, opt = {} ):
        return self.get("sequences/%d/administrators" % (sequence_id), opt)

     # Method: add_sequence_administrator
     #     Add admin to sequence
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    sequence_id - _integer_ (Required) The equence identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def add_sequence_administrator( self, sequence_id, administrator_id ):
        return self.put("sequences/%d/administrators/%d" % (sequence_id, administrator_id))

     # Method: remove_sequence_administrator
     #     Remove admin from sequence
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    sequence_id - _integer_ (Required) The equence identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def remove_sequence_administrator( self, sequence_id, administrator_id ):
        return self.delete("sequences/%d/administrators/%d" % (sequence_id, administrator_id))

     # Method: list_sequence_collaborations
     #     Retrieve list of collaborations this sequence is a part of
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    sequence_id - _integer_ (Required) The equence identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Collaboration List Response
    def list_sequence_collaborations( self, sequence_id, opt = {} ):
        return self.get("sequences/%d/collaborations" % (sequence_id), opt)

     # Method: list_sequence_datasets
     #     Retrieve list of datasets this sequence is a part of
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    sequence_id - _integer_ (Required) The equence identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Dataset List Response
    def list_sequence_datasets( self, sequence_id, opt = {} ):
        return self.get("sequences/%d/datasets" % (sequence_id), opt)

     # Method: list_hits
     #     Retrieve list of hits
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Hit List Response
    def list_hits( self, opt = {} ):
        return self.get("hits", opt)

     # Method: get_hit
     #     Retrieve single, specific hit
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    hit_id - _integer_ (Required) The it identifier.
     #
     # Returns:
     #     Hit Instance Response
    def get_hit( self, hit_id ):
        return self.get("hits/%d" % (hit_id))

     # Method: list_hit_administrators
     #     Retrieve list of administrators for this hit
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    hit_id - _integer_ (Required) The it identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Administrator List Response
    def list_hit_administrators( self, hit_id, opt = {} ):
        return self.get("hits/%d/administrators" % (hit_id), opt)

     # Method: add_hit_administrator
     #     Add admin to hit
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    hit_id - _integer_ (Required) The it identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def add_hit_administrator( self, hit_id, administrator_id ):
        return self.put("hits/%d/administrators/%d" % (hit_id, administrator_id))

     # Method: remove_hit_administrator
     #     Remove admin from hit
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    hit_id - _integer_ (Required) The it identifier.
     #    administrator_id - _integer_ (Required) The dministrator identifier.
     #
     # Returns:
     #     Administrator List Response
    def remove_hit_administrator( self, hit_id, administrator_id ):
        return self.delete("hits/%d/administrators/%d" % (hit_id, administrator_id))

     # Method: list_hit_collaborations
     #     Retrieve list of collaborations this hit is a part of
     #
     # Access:
     #     Public
     #
     # Parameters:
     #    hit_id - _integer_ (Required) The it identifier.
     #    opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
     #
     # Keys for the opt parameter:
     #    created - _boolean_ (Optional) todo
     #    page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
     #    page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
     #    public - _boolean_ (Optional) todo
     #    shared - _boolean_ (Optional) todo
     #
     # Returns:
     #     Collaboration List Response
    def list_hit_collaborations( self, hit_id, opt = {} ):
        return self.get("hits/%d/collaborations" % (hit_id), opt)

