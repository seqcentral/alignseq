<?php

/* Read in our credentials */
$config = parse_ini_file(__DIR__.'/../../alignseq.conf', TRUE);

/* Load the SeqCentral AlignSeq API */
require(__DIR__.'/../alignseq.php');

/* Create an AlignSeq Client to make requests for us */
$alignseq_client = new AlignSeq($config['oauth']);

/* Make a request and save the response */
$response = $alignseq_client->list_datasets();

/* Act on the response... */
print_r($response);