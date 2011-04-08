<?php

require(__DIR__.'/../oauthsimple/php/OAuthSimple.php');

class AlignSeq_OAuth {

	private $_consumer = NULL;

	public function __construct($consumer_key, $consumer_secret) {
		$this->_consumer = new OAuthSimple($consumer_key, $consumer_secret);
	}

	public function make_request($method, $url, $opt) {
		$method = strtoupper($method);

		$this->_consumer->reset();

		$obj = $this->_consumer->sign(array(
			'action'=> $method,
			'path'=> $url,
			'parameters'=> $opt
		));

		$ch = curl_init();
		curl_setopt_array($ch, array(
			CURLOPT_TIMEOUT => 30,
			CURLOPT_CUSTOMREQUEST => $method,
			CURLOPT_URL => ($method === 'POST') ? $url : $obj['signed_url'],
			CURLOPT_HTTPHEADER => array(
				'Authorization' => $obj['header']
			),
			CURLOPT_RETURNTRANSFER => TRUE,
			CURLOPT_FAILONERROR => FALSE
		));

		if($method === 'POST') {
			curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($obj['parameters'], NULL, '&'));
		}

		$r = curl_exec($ch);
		$s = curl_getinfo($ch, CURLINFO_HTTP_CODE);

		curl_close($ch);
		return (object) array('status' => $s, 'body' => $r);
	}

}
