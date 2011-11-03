<?php

/* Read in our credentials */
$config = parse_ini_file(__DIR__.'/../../alignseq.conf', TRUE);

/* Load the SeqCentral AlignSeq API */
require(__DIR__.'/../alignseq.php');

/* Create an AlignSeq Client to make requests for us */
$alignseq_client = new AlignSeq($config['oauth']);

$resources = array('collaborations', 'datasets', 'executables', 'hits', 'jobs', 'sequences', 'users');
// $resources = array('sequences');

foreach ($resources as $resource)
{
	/* Make a request and save the response */
	$response = $alignseq_client->options($resource);

	/* Act on the response... */
	if (empty($response)) {
		print_r($alignseq_client->response);
	}

	/* Make a request and save the response */
	$response = $alignseq_client->options($resource.'/1');

	/* Act on the response... */
	if (empty($response)) {
		print_r($alignseq_client->response);
	}

	foreach ($resources as $subresource)
	{
		/* Make a request and save the response */
		$response = $alignseq_client->options($resource.'/1/'.$subresource);

		/* Act on the response... */
		if (empty($response)) {
			print_r($alignseq_client->response);
		}

		/* Make a request and save the response */
		$response = $alignseq_client->options($resource.'/1/'.$subresource.'/1');

		/* Act on the response... */
		if (empty($response)) {
			print_r($alignseq_client->response);
		}


	}


}
