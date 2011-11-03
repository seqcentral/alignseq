&lt;?php
require('PATH/TO/php/alignseq.php');

$alignseq = new AlignSeq(array(
	'consumer_key' => 'YOUR CONSUMER KEY',
	'consumer_secret' => 'YOUR CONSUMER SECRET'
));

// Job ID to retrieve
$job_id = XX;

// Loop over all pages, starting at page #0
$page = 0;
do {
	// get next page of hits
	$hits = $alignseq->list_job_hits($job_id, array('page' => $page));
	// do something with hits->data
	print($hits->data->page."\n");
	// set index to next page
	$page++;
	
} while($page < $hits->data->total_pages);
