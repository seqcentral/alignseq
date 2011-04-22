<?php

// This requires the OAuth PECL package: http://www.php.net/oauth

class AlignSeq_OAuth {

	private $_consumer = NULL;

	public function __construct($consumer_key, $consumer_secret) {
		$this->_consumer = new OAuth($consumer_key, $consumer_secret);
	}

	private function flatten_array($arr, $prefix = NULL) {
		$flattened = array();
		foreach($arr as $k => $v) {
			$name = ($prefix) ? $prefix.'['.$k.']' : $k;
			if (is_array($v)) {
				$flattened = array_merge($flattened, $this->flatten_array($v, $name));
			} else {
				$flattened[$name] = $v;
			}
		}
		return $flattened;
	}

	public function make_request($method, $url, $opt) {
		$method = strtoupper($method);
		switch($method) {
			case 'GET': $method = OAUTH_HTTP_METHOD_GET; break;
			case 'POST': $method = OAUTH_HTTP_METHOD_POST; break;
			case 'PUT': $method = OAUTH_HTTP_METHOD_PUT; break;
			case 'DELETE': $method = OAUTH_HTTP_METHOD_DELETE; break;
			default: return false;
		}

		try {
			$this->_consumer->fetch($url, $this->flatten_array($opt), $method);
			$r = $this->_consumer->getLastResponse();
			$s = $this->_consumer->getLastResponseInfo();
		} catch(OAuthException $E) {
			// As far as I can tell, the OAuthException data is inaccessible except for lastResponse.
			// Since $E->lastResponse is the same as $this->_consumer->getLastResponse(),
			// I'm simply ignoring the exception that occurs if HTTP status is not 20x.
			// Let me know if this is incorrect:  https://github.com/seqcentral/alignseq/issues
			// print_r($E);
			$r = $this->_consumer->getLastResponse();
			$s = $this->_consumer->getLastResponseInfo();
		}

		return (object) array('status' => $s, 'body' => $r);
	}

}
