# coding: utf-8

"""
	Copyright 2018 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	  <http://www.apache.org/licenses/LICENSE-2.0>
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""
from __future__ import absolute_import
import sys
import os
import re
from six import iteritems

class SecurityMappingApi(object):
	def __init__(self, api_client):
		self.api_client = api_client

	def get_by_path(self, path, selected_fields, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_by_path_with_http_info(path, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_by_path_with_http_info(path, selected_fields, web_id_type, **kwargs)
			return data

	def get_by_path_with_http_info(self, path, selected_fields, web_id_type, **kwargs):
		all_params = ['path', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_by_path_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('path' not in params) or (params['path'] is None):
			raise ValueError("Missing the required parameter `path` when calling `get_by_path_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'path' in params:
			if (params['path'] is not None):
				query_params['path'] = params['path']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/securitymappings', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PISecurityMapping',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get(self, web_id, selected_fields, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_with_http_info(self, web_id, selected_fields, web_id_type, **kwargs):
		all_params = ['web_id', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/securitymappings/{webId}', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PISecurityMapping',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update(self, web_id, security_mapping, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_with_http_info(web_id, security_mapping, **kwargs)
		else:
			(data) = self.update_with_http_info(web_id, security_mapping, **kwargs)
			return data

	def update_with_http_info(self, web_id, security_mapping, **kwargs):
		all_params = ['web_id', 'security_mapping']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method update_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `update_with_http_info`")
		if ('security_mapping' not in params) or (params['security_mapping'] is None):
			raise ValueError("Missing the required parameter `security_mapping` when calling `update_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'security_mapping' in params:
			body_params = params['security_mapping']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/securitymappings/{webId}', 'PATCH',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type =None,
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def delete(self, web_id, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.delete_with_http_info(web_id, **kwargs)
		else:
			(data) = self.delete_with_http_info(web_id, **kwargs)
			return data

	def delete_with_http_info(self, web_id, **kwargs):
		all_params = ['web_id']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method delete_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `delete_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/securitymappings/{webId}', 'DELETE',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type =None,
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_security(self, web_id, user_identity, force_refresh, selected_fields, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_with_http_info(web_id, user_identity, force_refresh, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_with_http_info(web_id, user_identity, force_refresh, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_with_http_info(self, web_id, user_identity, force_refresh, selected_fields, web_id_type, **kwargs):
		all_params = ['web_id', 'user_identity', 'force_refresh', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_with_http_info`")
		if ('user_identity' not in params) or (params['user_identity'] is None):
			raise ValueError("Missing the required parameter `user_identity` when calling `get_security_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'user_identity' in params:
			if (params['user_identity'] is not None):
				query_params['userIdentity'] = params['user_identity']
				collection_formats['userIdentity'] = 'multi'
		if 'force_refresh' in params:
			if (params['force_refresh'] is not None):
				query_params['forceRefresh'] = params['force_refresh']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/securitymappings/{webId}/security', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSecurityRights',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_security_entries(self, web_id, name_filter, selected_fields, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_entries_with_http_info(web_id, name_filter, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_entries_with_http_info(web_id, name_filter, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_entries_with_http_info(self, web_id, name_filter, selected_fields, web_id_type, **kwargs):
		all_params = ['web_id', 'name_filter', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_entries_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_entries_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/securitymappings/{webId}/securityentries', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSecurityEntry',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_security_entry_by_name(self, name, web_id, selected_fields, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_entry_by_name_with_http_info(name, web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_entry_by_name_with_http_info(name, web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_entry_by_name_with_http_info(self, name, web_id, selected_fields, web_id_type, **kwargs):
		all_params = ['name', 'web_id', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_entry_by_name_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('name' not in params) or (params['name'] is None):
			raise ValueError("Missing the required parameter `name` when calling `get_security_entry_by_name_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_entry_by_name_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'name' in params:
			if (params['name'] is not None):
				path_params['name'] = params['name']
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/securitymappings/{webId}/securityentries/{name}', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PISecurityEntry',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)

