<?php

require 'alignseq_oauth.php';

class AlignSeq {

	const NUCL_SEQ = 1;
	const PROT_SEQ = 2;

	const VERSION = '1.0-rc3';
	const SERVER = 'http://api.seqcentral.com/alignseq';
	// const SERVER = 'http://api.localhost/alignseq';

	public $url = '';
	public $response = '';

	private $_oauth = NULL;

	public function __construct( $params ) {
		/* If you wish to use your own OAuth client, make your changes here and in 'make_oauth_request()' */
		if (array_key_exists('consumer_key', $params) && array_key_exists('consumer_secret', $params)) {
			$this->_oauth = new AlignSeq_OAuth($params['consumer_key'], $params['consumer_secret']);
		} else {
			print 'Incorrect parameters';
		}
	}

	/**
	 * Method: make_oauth_request
	 *	Make an OAuth authenticated request to the SeqCentral REST service.
	 *
	 * Access:
	 * 	Private
	 *
	 * Parameters:
	 *	$method - _string_ (Required) The HTTP request method type: 'get', 'post', 'put', or 'delete'
	 *	$url - _string_ (Required) The url to direct the request to.
	 *	$opt - _array_ (Required) An associative array of parameters whose keys depend on the URI accessed.
	 *
	 * Returns:
	 *	Object containing parsed Response
	 */
	private function make_oauth_request( $method, $url, $opt ) {
		$this->url = $url;
		/* If you wish to use your own OAuth client, make your changes here and in '__construct()' */
		$this->response = $this->_oauth->make_request($method, $url, (!empty($opt)) ? array('json' => json_encode($opt)) : NULL);
		return json_decode($this->response->body);
	}

	public function options( $uri, $opt = array() ) {
		return $this->make_oauth_request('options', self::SERVER.'/'.self::VERSION.'/'.$uri, $opt);
	}


	/**
	 * Method: get
	 *	Generic method to send an HTTP GET request to the SeqCentral REST service.
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$uri - _string_ (Required) The location of the resource to access.
	 *	$opt - _array_ (Optional) An associative array of parameters whose keys depend on the URI accessed.
	 *
	 * Returns:
	 *
	 */
	public function get( $uri, $opt = array() ) {
		return $this->make_oauth_request('get', self::SERVER.'/'.self::VERSION.'/'.$uri, $opt);
	}

	/**
	 * Method: post
	 *	Generic method to send an HTTP POST request to the SeqCentral REST service.
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$uri - _string_ (Required) The location of the resource to access.
	 *	$opt - _array_ (Optional) An associative array of parameters whose keys depend on the URI accessed.
	 *
	 * Returns:
	 *
	 */
	public function post( $uri, $opt = array() ) {
		return $this->make_oauth_request('post', self::SERVER.'/'.self::VERSION.'/'.$uri, $opt);
	}

	/**
	 * Method: put
	 *	Generic method to send an HTTP PUT request to the SeqCentral REST service.
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$uri - _string_ (Required) The location of the resource to access.
	 *	$opt - _array_ (Optional) An associative array of parameters whose keys depend on the URI accessed.
	 *
	 * Returns:
	 *
	 */
	public function put( $uri, $opt = array() ) {
		return $this->make_oauth_request('put', self::SERVER.'/'.self::VERSION.'/'.$uri, $opt);
	}

	/**
	 * Method: delete
	 *	Generic method to send an HTTP DELETE request to the SeqCentral REST service.
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$uri - _string_ (Required) The location of the resource to access.
	 *	$opt - _array_ (Optional) An associative array of parameters whose keys depend on the URI accessed.
	 *
	 * Returns:
	 *
	 */
	public function delete( $uri, $opt = array() ) {
		return $this->make_oauth_request('delete', self::SERVER.'/'.self::VERSION.'/'.$uri, $opt);
	}

	/**
	 * Method: list_users
	 * 	Retrieve list of users
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function list_users( $opt = array() ) {
		return $this->get("users", $opt);
	}

	/**
	 * Method: create_user
	 * 	Create new user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$username - _string_ (Required) todo
	 *	$email - _string_ (Required) todo
	 *	$password - _string_ (Required) todo
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	keep_in_loop - _boolean_ (Optional) todo
	 *
	 * Returns:
	 * 	User Instance Response
	 */
	public function create_user( $username, $email, $password, $opt = array() ) {
		$opt['username'] = $username;
		$opt['email'] = $email;
		$opt['password'] = $password;
		return $this->post("users", $opt);
	}

	/**
	 * Method: get_user
	 * 	Retrieve single, specific user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User Instance Response
	 */
	public function get_user( $user_id ) {
		return $this->get("users/$user_id");
	}

	/**
	 * Method: update_user
	 * 	Update user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	affiliation - _string_ (Optional) todo
	 *	keep_in_loop - _boolean_ (Optional) todo
	 *	name - _string_ (Optional) todo
	 *
	 * Returns:
	 * 	User Instance Response
	 */
	public function update_user( $user_id, $opt = array() ) {
		return $this->post("users/$user_id", $opt);
	}

	/**
	 * Method: delete_user
	 * 	Delete user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function delete_user( $user_id ) {
		return $this->delete("users/$user_id");
	}

	/**
	 * Method: list_user_users
	 * 	Retrieve list of users that have special access to this user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function list_user_users( $user_id, $opt = array() ) {
		return $this->get("users/$user_id/users", $opt);
	}

	/**
	 * Method: add_user_user
	 * 	Add admin to user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$admin_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function add_user_user( $user_id, $admin_id ) {
		return $this->put("users/$user_id/users/$admin_id");
	}

	/**
	 * Method: remove_user_user
	 * 	Remove admin from user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$admin_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function remove_user_user( $user_id, $admin_id ) {
		return $this->delete("users/$user_id/users/$admin_id");
	}

	/**
	 * Method: list_user_collaborations
	 * 	Retrieve list of collaborations that have special access to this user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function list_user_collaborations( $user_id, $opt = array() ) {
		return $this->get("users/$user_id/collaborations", $opt);
	}

	/**
	 * Method: add_user_collaboration
	 * 	Add collaborations to user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function add_user_collaboration( $user_id, $collaboration_id ) {
		return $this->put("users/$user_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: remove_user_collaboration
	 * 	Remove collaborations from user
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function remove_user_collaboration( $user_id, $collaboration_id ) {
		return $this->delete("users/$user_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: list_user_jobs
	 * 	Retrieve list of jobs this user has access to
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Job List Response
	 */
	public function list_user_jobs( $user_id, $opt = array() ) {
		return $this->get("users/$user_id/jobs", $opt);
	}

	/**
	 * Method: list_user_datasets
	 * 	Retrieve list of datasets this user has access to
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Dataset List Response
	 */
	public function list_user_datasets( $user_id, $opt = array() ) {
		return $this->get("users/$user_id/datasets", $opt);
	}

	/**
	 * Method: list_user_executables
	 * 	Retrieve list of executables this user has access to
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$user_id - _integer_ (Required) The user identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Executable List Response
	 */
	public function list_user_executables( $user_id, $opt = array() ) {
		return $this->get("users/$user_id/executables", $opt);
	}

	/**
	 * Method: list_collaborations
	 * 	Retrieve list of collaborations
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function list_collaborations( $opt = array() ) {
		return $this->get("collaborations", $opt);
	}

	/**
	 * Method: create_collaboration
	 * 	Create new collaboration
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$name - _string_ (Required) Short human-readable name of collaboration.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	description - _string_ (Optional) Longer human-readable description of collaboration.
	 *
	 * Returns:
	 * 	Collaboration Instance Response
	 */
	public function create_collaboration( $name, $opt = array() ) {
		$opt['name'] = $name;
		return $this->post("collaborations", $opt);
	}

	/**
	 * Method: get_collaboration
	 * 	Retrieve single, specific collaboration
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration Instance Response
	 */
	public function get_collaboration( $collaboration_id ) {
		return $this->get("collaborations/$collaboration_id");
	}

	/**
	 * Method: update_collaboration
	 * 	Update collaboration
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	description - _string_ (Optional) Longer human-readable description of collaboration.
	 *	name - _string_ (Optional) Short human-readable name of collaboration.
	 *
	 * Returns:
	 * 	Collaboration Instance Response
	 */
	public function update_collaboration( $collaboration_id, $opt = array() ) {
		return $this->post("collaborations/$collaboration_id", $opt);
	}

	/**
	 * Method: delete_collaboration
	 * 	Delete collaboration
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function delete_collaboration( $collaboration_id ) {
		return $this->delete("collaborations/$collaboration_id");
	}

	/**
	 * Method: list_collaboration_users
	 * 	Retrieve list of users that have special access to this collaboration
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function list_collaboration_users( $collaboration_id, $opt = array() ) {
		return $this->get("collaborations/$collaboration_id/users", $opt);
	}

	/**
	 * Method: add_collaboration_user
	 * 	Add admin to collaboration
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function add_collaboration_user( $collaboration_id, $user_id ) {
		return $this->put("collaborations/$collaboration_id/users/$user_id");
	}

	/**
	 * Method: remove_collaboration_user
	 * 	Remove admin from collaboration
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function remove_collaboration_user( $collaboration_id, $user_id ) {
		return $this->delete("collaborations/$collaboration_id/users/$user_id");
	}

	/**
	 * Method: list_collaboration_collaborations
	 * 	Retrieve list of collaborations that have special access to this collaborations
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function list_collaboration_collaborations( $collaboration_id, $opt = array() ) {
		return $this->get("collaborations/$collaboration_id/collaborations", $opt);
	}

	/**
	 * Method: add_collaboration_collaboration
	 * 	Add collaborations to collaborations
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *	$collaboration_id2 - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function add_collaboration_collaboration( $collaboration_id, $collaboration_id2 ) {
		return $this->put("collaborations/$collaboration_id/collaborations/$collaboration_id2");
	}

	/**
	 * Method: remove_collaboration_collaboration
	 * 	Remove collaborations from collaborations
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *	$collaboration_id2 - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function remove_collaboration_collaboration( $collaboration_id, $collaboration_id2 ) {
		return $this->delete("collaborations/$collaboration_id/collaborations/$collaboration_id2");
	}

	/**
	 * Method: list_jobs
	 * 	Retrieve list of jobs
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Job List Response
	 */
	public function list_jobs( $opt = array() ) {
		return $this->get("jobs", $opt);
	}

	/**
	 * Method: create_job
	 * 	Create new job
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$name - _string_ (Required) Short human-readable name of job
	 *	$executable_id - _integer_ (Required) Identifier of executable to use
	 *	$queries - _array_ (Required) Array of dataset ids to use as queries
	 *	$targets - _array_ (Required) Array of of dataset ids to use as targets
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	description - _string_ (Optional) Longer human-readable description of job
	 *	executable_parameters - _array_ (Optional) Array of search parameters specific to executable
	 *	notify - _boolean_ (Optional) Be notified via email when job is completed
	 *
	 * Returns:
	 * 	Job Instance Response
	 */
	public function create_job( $name, $executable_id, $queries, $targets, $opt = array() ) {
		$opt['name'] = $name;
		$opt['executable_id'] = $executable_id;
		$opt['queries'] = $queries;
		$opt['targets'] = $targets;
		return $this->post("jobs", $opt);
	}

	/**
	 * Method: get_job
	 * 	Retrieve single, specific job
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *
	 * Returns:
	 * 	Job Instance Response
	 */
	public function get_job( $job_id ) {
		return $this->get("jobs/$job_id");
	}

	/**
	 * Method: update_job
	 * 	Update job
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	description - _string_ (Optional) Longer human-readable description of job
	 *	name - _string_ (Optional) Short human-readable name of job
	 *	notify - _boolean_ (Optional) Be notified via email when job is completed
	 *	public - _boolean_ (Optional) todo
	 *
	 * Returns:
	 * 	Job Instance Response
	 */
	public function update_job( $job_id, $opt = array() ) {
		return $this->post("jobs/$job_id", $opt);
	}

	/**
	 * Method: delete_job
	 * 	Delete job
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *
	 * Returns:
	 * 	Job List Response
	 */
	public function delete_job( $job_id ) {
		return $this->delete("jobs/$job_id");
	}

	/**
	 * Method: list_job_users
	 * 	Retrieve list of users that have special access to this jobs
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function list_job_users( $job_id, $opt = array() ) {
		return $this->get("jobs/$job_id/users", $opt);
	}

	/**
	 * Method: add_job_user
	 * 	Add admin to jobs
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function add_job_user( $job_id, $user_id ) {
		return $this->put("jobs/$job_id/users/$user_id");
	}

	/**
	 * Method: remove_job_user
	 * 	Remove admin from jobs
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function remove_job_user( $job_id, $user_id ) {
		return $this->delete("jobs/$job_id/users/$user_id");
	}

	/**
	 * Method: list_job_collaborations
	 * 	Retrieve list of collaborations that have special access to this jobs
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function list_job_collaborations( $job_id, $opt = array() ) {
		return $this->get("jobs/$job_id/collaborations", $opt);
	}

	/**
	 * Method: add_job_collaboration
	 * 	Add collaborations to jobs
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function add_job_collaboration( $job_id, $collaboration_id ) {
		return $this->put("jobs/$job_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: remove_job_collaboration
	 * 	Remove collaborations from jobs
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function remove_job_collaboration( $job_id, $collaboration_id ) {
		return $this->delete("jobs/$job_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: list_job_hits
	 * 	Retrieve list of hits this job created
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$job_id - _integer_ (Required) The job identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Hit List Response
	 */
	public function list_job_hits( $job_id, $opt = array() ) {
		return $this->get("jobs/$job_id/hits", $opt);
	}

	/**
	 * Method: list_datasets
	 * 	Retrieve list of datasets
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	datatype - _integer_ (Optional) Type of data represented by sequences in dataset: 1 = nucleotide, 2 = protein
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Dataset List Response
	 */
	public function list_datasets( $opt = array() ) {
		return $this->get("datasets", $opt);
	}

	/**
	 * Method: create_dataset
	 * 	Create new dataset
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$name - _string_ (Required) Short human-readable name of dataset
	 *	$datatype - _integer_ (Required) Type of data represented by sequences in dataset: 1 = nucleotide, 2 = protein
	 *	$files - _array_ (Required) Array of 2-element arrays of source files and their MD5 signatures
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	description - _string_ (Optional) Longer human-readable description of dataset
	 *	public - _boolean_ (Optional) todo
	 *	source - _string_ (Optional) Source of dataset. E.g., VBI, Broad, JCVI
	 *	version - _string_ (Optional) Version descriptor of the dataset
	 *
	 * Returns:
	 * 	Dataset Instance Response
	 */
	public function create_dataset( $name, $datatype, $files, $opt = array() ) {
		$opt['name'] = $name;
		$opt['datatype'] = $datatype;
		$opt['files'] = $files;
		return $this->post("datasets", $opt);
	}

	/**
	 * Method: get_dataset
	 * 	Retrieve single, specific dataset
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *
	 * Returns:
	 * 	Dataset Instance Response
	 */
	public function get_dataset( $dataset_id ) {
		return $this->get("datasets/$dataset_id");
	}

	/**
	 * Method: update_dataset
	 * 	Update dataset
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	description - _string_ (Optional) Longer human-readable description of dataset
	 *	name - _string_ (Optional) Short human-readable name of dataset
	 *	public - _boolean_ (Optional) todo
	 *
	 * Returns:
	 * 	Dataset Instance Response
	 */
	public function update_dataset( $dataset_id, $opt = array() ) {
		return $this->post("datasets/$dataset_id", $opt);
	}

	/**
	 * Method: delete_dataset
	 * 	Delete dataset
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *
	 * Returns:
	 * 	Dataset List Response
	 */
	public function delete_dataset( $dataset_id ) {
		return $this->delete("datasets/$dataset_id");
	}

	/**
	 * Method: list_dataset_users
	 * 	Retrieve list of users that have special access to this datasets
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function list_dataset_users( $dataset_id, $opt = array() ) {
		return $this->get("datasets/$dataset_id/users", $opt);
	}

	/**
	 * Method: add_dataset_user
	 * 	Add admin to datasets
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function add_dataset_user( $dataset_id, $user_id ) {
		return $this->put("datasets/$dataset_id/users/$user_id");
	}

	/**
	 * Method: remove_dataset_user
	 * 	Remove admin from datasets
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function remove_dataset_user( $dataset_id, $user_id ) {
		return $this->delete("datasets/$dataset_id/users/$user_id");
	}

	/**
	 * Method: list_dataset_collaborations
	 * 	Retrieve list of collaborations that have special access to this datasets
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function list_dataset_collaborations( $dataset_id, $opt = array() ) {
		return $this->get("datasets/$dataset_id/collaborations", $opt);
	}

	/**
	 * Method: add_dataset_collaboration
	 * 	Add collaborations to datasets
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function add_dataset_collaboration( $dataset_id, $collaboration_id ) {
		return $this->put("datasets/$dataset_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: remove_dataset_collaboration
	 * 	Remove collaborations from datasets
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function remove_dataset_collaboration( $dataset_id, $collaboration_id ) {
		return $this->delete("datasets/$dataset_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: list_dataset_sequences
	 * 	Retrieve list of sequences this dataset contains
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$dataset_id - _integer_ (Required) The dataset identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Sequence List Response
	 */
	public function list_dataset_sequences( $dataset_id, $opt = array() ) {
		return $this->get("datasets/$dataset_id/sequences", $opt);
	}

	/**
	 * Method: list_executables
	 * 	Retrieve list of executables
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	datatype_query - _integer_ (Optional) todo
	 *	datatype_target - _integer_ (Optional) todo
	 *	institution - _string_ (Optional) todo
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Executable List Response
	 */
	public function list_executables( $opt = array() ) {
		return $this->get("executables", $opt);
	}

	/**
	 * Method: create_executable
	 * 	Create new executable
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$name - _string_ (Required) todo
	 *	$version - _string_ (Required) todo
	 *	$datatype_query - _integer_ (Required) todo
	 *	$datatype_target - _integer_ (Required) todo
	 *	$factor - _float_ (Required) todo
	 *	$input_parameters - _array_ (Required) todo
	 *	$output_parameters - _array_ (Required) todo
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	institution - _string_ (Optional) todo
	 *	public - _boolean_ (Optional) todo
	 *
	 * Returns:
	 * 	Executable Instance Response
	 */
	public function create_executable( $name, $version, $datatype_query, $datatype_target, $factor, $input_parameters, $output_parameters, $opt = array() ) {
		$opt['name'] = $name;
		$opt['version'] = $version;
		$opt['datatype_query'] = $datatype_query;
		$opt['datatype_target'] = $datatype_target;
		$opt['factor'] = $factor;
		$opt['input_parameters'] = $input_parameters;
		$opt['output_parameters'] = $output_parameters;
		return $this->post("executables", $opt);
	}

	/**
	 * Method: get_executable
	 * 	Retrieve single, specific executable
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *
	 * Returns:
	 * 	Executable Instance Response
	 */
	public function get_executable( $executable_id ) {
		return $this->get("executables/$executable_id");
	}

	/**
	 * Method: update_executable
	 * 	Update executable
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	description - _string_ (Optional) todo
	 *	name - _string_ (Optional) todo
	 *	public - _boolean_ (Optional) todo
	 *
	 * Returns:
	 * 	Executable Instance Response
	 */
	public function update_executable( $executable_id, $opt = array() ) {
		return $this->post("executables/$executable_id", $opt);
	}

	/**
	 * Method: delete_executable
	 * 	Delete executable
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *
	 * Returns:
	 * 	Executable List Response
	 */
	public function delete_executable( $executable_id ) {
		return $this->delete("executables/$executable_id");
	}

	/**
	 * Method: list_executable_users
	 * 	Retrieve list of users that have special access to this executables
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function list_executable_users( $executable_id, $opt = array() ) {
		return $this->get("executables/$executable_id/users", $opt);
	}

	/**
	 * Method: add_executable_user
	 * 	Add admin to executables
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function add_executable_user( $executable_id, $user_id ) {
		return $this->put("executables/$executable_id/users/$user_id");
	}

	/**
	 * Method: remove_executable_user
	 * 	Remove admin from executables
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function remove_executable_user( $executable_id, $user_id ) {
		return $this->delete("executables/$executable_id/users/$user_id");
	}

	/**
	 * Method: list_executable_collaborations
	 * 	Retrieve list of collaborations that have special access to this executables
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function list_executable_collaborations( $executable_id, $opt = array() ) {
		return $this->get("executables/$executable_id/collaborations", $opt);
	}

	/**
	 * Method: add_executable_collaboration
	 * 	Add collaborations to executables
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function add_executable_collaboration( $executable_id, $collaboration_id ) {
		return $this->put("executables/$executable_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: remove_executable_collaboration
	 * 	Remove collaborations from executables
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$executable_id - _integer_ (Required) The executable identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function remove_executable_collaboration( $executable_id, $collaboration_id ) {
		return $this->delete("executables/$executable_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: list_sequences
	 * 	Retrieve list of sequences
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Sequence List Response
	 */
	public function list_sequences( $opt = array() ) {
		return $this->get("sequences", $opt);
	}

	/**
	 * Method: get_sequence
	 * 	Retrieve single, specific sequence
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *
	 * Returns:
	 * 	Sequence Instance Response
	 */
	public function get_sequence( $sequence_id ) {
		return $this->get("sequences/$sequence_id");
	}

	/**
	 * Method: update_sequence
	 * 	Update sequences
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	name - _string_ (Optional) todo
	 *
	 * Returns:
	 * 	Sequence Instance Response
	 */
	public function update_sequence( $sequence_id, $opt = array() ) {
		return $this->post("sequences/$sequence_id", $opt);
	}

	/**
	 * Method: delete_sequence
	 * 	Delete sequence
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *
	 * Returns:
	 * 	Sequence List Response
	 */
	public function delete_sequence( $sequence_id ) {
		return $this->delete("sequences/$sequence_id");
	}

	/**
	 * Method: list_sequence_users
	 * 	Retrieve list of users that have special access to this sequences
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function list_sequence_users( $sequence_id, $opt = array() ) {
		return $this->get("sequences/$sequence_id/users", $opt);
	}

	/**
	 * Method: add_sequence_user
	 * 	Add admin to sequences
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function add_sequence_user( $sequence_id, $user_id ) {
		return $this->put("sequences/$sequence_id/users/$user_id");
	}

	/**
	 * Method: remove_sequence_user
	 * 	Remove admin from sequences
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function remove_sequence_user( $sequence_id, $user_id ) {
		return $this->delete("sequences/$sequence_id/users/$user_id");
	}

	/**
	 * Method: list_sequence_collaborations
	 * 	Retrieve list of collaborations that have special access to this sequences
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function list_sequence_collaborations( $sequence_id, $opt = array() ) {
		return $this->get("sequences/$sequence_id/collaborations", $opt);
	}

	/**
	 * Method: add_sequence_collaboration
	 * 	Add collaborations to sequences
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function add_sequence_collaboration( $sequence_id, $collaboration_id ) {
		return $this->put("sequences/$sequence_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: remove_sequence_collaboration
	 * 	Remove collaborations from sequences
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$sequence_id - _integer_ (Required) The sequence identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function remove_sequence_collaboration( $sequence_id, $collaboration_id ) {
		return $this->delete("sequences/$sequence_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: list_hits
	 * 	Retrieve list of hits
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Hit List Response
	 */
	public function list_hits( $opt = array() ) {
		return $this->get("hits", $opt);
	}

	/**
	 * Method: get_hit
	 * 	Retrieve single, specific hit
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$hit_id - _integer_ (Required) The hit identifier.
	 *
	 * Returns:
	 * 	Hit Instance Response
	 */
	public function get_hit( $hit_id ) {
		return $this->get("hits/$hit_id");
	}

	/**
	 * Method: list_hit_users
	 * 	Retrieve list of users that have special access to this hits
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$hit_id - _integer_ (Required) The hit identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function list_hit_users( $hit_id, $opt = array() ) {
		return $this->get("hits/$hit_id/users", $opt);
	}

	/**
	 * Method: add_hit_user
	 * 	Add admin to hits
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$hit_id - _integer_ (Required) The hit identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function add_hit_user( $hit_id, $user_id ) {
		return $this->put("hits/$hit_id/users/$user_id");
	}

	/**
	 * Method: remove_hit_user
	 * 	Remove admin from hits
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$hit_id - _integer_ (Required) The hit identifier.
	 *	$user_id - _integer_ (Required) The user identifier.
	 *
	 * Returns:
	 * 	User List Response
	 */
	public function remove_hit_user( $hit_id, $user_id ) {
		return $this->delete("hits/$hit_id/users/$user_id");
	}

	/**
	 * Method: list_hit_collaborations
	 * 	Retrieve list of collaborations that have special access to this hits
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$hit_id - _integer_ (Required) The hit identifier.
	 *	$opt - _array_ (Optional) An associative array of parameters that can have the keys listed in the following section.
	 *
	 * Keys for the $opt parameter:
	 *	page - _integer_ (Optional) Which page to view. Zero-indexed, so the first page is 0.
	 *	page_size - _integer_ (Optional) How many resources to return in each list page. The maximum is 1000.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function list_hit_collaborations( $hit_id, $opt = array() ) {
		return $this->get("hits/$hit_id/collaborations", $opt);
	}

	/**
	 * Method: add_hit_collaboration
	 * 	Add collaborations to hits
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$hit_id - _integer_ (Required) The hit identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function add_hit_collaboration( $hit_id, $collaboration_id ) {
		return $this->put("hits/$hit_id/collaborations/$collaboration_id");
	}

	/**
	 * Method: remove_hit_collaboration
	 * 	Remove collaborations from hits
	 *
	 * Access:
	 * 	Public
	 *
	 * Parameters:
	 *	$hit_id - _integer_ (Required) The hit identifier.
	 *	$collaboration_id - _integer_ (Required) The collaboration identifier.
	 *
	 * Returns:
	 * 	Collaboration List Response
	 */
	public function remove_hit_collaboration( $hit_id, $collaboration_id ) {
		return $this->delete("hits/$hit_id/collaborations/$collaboration_id");
	}

}
