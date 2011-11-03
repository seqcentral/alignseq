<?php

/* Read in our credentials */
$config = parse_ini_file(__DIR__.'/../../alignseq.conf', TRUE);

/* Load the SeqCentral AlignSeq API */
require(__DIR__.'/../alignseq.php');

/* Create an AlignSeq Client to make requests for us */
$alignseq_client = new AlignSeq($config['oauth']);

/* Keep track of our files */
$my_files = array(
	array(
		'filename' => '/tmp/Benchmark.nt.100',
		'md5' => md5_file('/tmp/benchmark.nt.100')
	),
	array(
		'filename' => '/tmp/mysql.sock',
		'md5' => md5_file('/tmp/benchmark.nt.100')
	)
);

/* Sanity check to ensure that files exist */
foreach ($my_files as $file)
{
	if (! file_exists($file['filename']))
	{
		print("**Error** Could not find: ".$file['filename']."\n");
		exit();
	}
}

/* Make a request and save the response */
$response = $alignseq_client->create_dataset("new dataset", AlignSeq::NUCL_SEQ, $my_files);

/* Act on the response... */
print_r($response);
print_r($alignseq_client->response);

/* Save the dataset id */
$dataset_id = $response->data->id;
print('Dataset #'.$dataset_id.' created'."\n");

/* Upload each file using the provided PUT url */
foreach ($response->data->files as $file)
{
	print('Uploading file '.$file->aws_put_url."\n");
	put($file->aws_put_url, file_from_md5($file->md5, $my_files));
}

print("Done\n");

/**********************/
function file_from_md5($md5, $files)
{
	foreach($files as $file)
	{
		if ($file['md5'] === $md5)
		{
			return $file['filename'];
		}
	}
	return NULL;
}

function put($url, $file) {
	$handle = curl_init();
	$filesize = filesize($file);
	$fh = fopen($file, 'r');

	if ($handle)
	{
		$curlOptArr = array(
			CURLOPT_URL => $url,
			CURLOPT_PUT => TRUE,
			CURLOPT_INFILESIZE => $filesize,
			CURLOPT_INFILE => $fh,
			CURLOPT_RETURNTRANSFER => TRUE
			);
		curl_setopt_array($handle, $curlOptArr);
		$ret = curl_exec($handle);
		$errRet = curl_error($handle);
		curl_close($handle);
	}
}
?>