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

class AnalysisTemplateApi(object):
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

		return self.api_client.call_api('/analysistemplates', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIAnalysisTemplate',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_from_analysis(self, analysis_web_id, name, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_from_analysis_with_http_info(analysis_web_id, name, web_id_type, **kwargs)
		else:
			(data) = self.create_from_analysis_with_http_info(analysis_web_id, name, web_id_type, **kwargs)
			return data

	def create_from_analysis_with_http_info(self, analysis_web_id, name, web_id_type, **kwargs):
		all_params = ['analysis_web_id', 'name', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_from_analysis_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('analysis_web_id' not in params) or (params['analysis_web_id'] is None):
			raise ValueError("Missing the required parameter `analysis_web_id` when calling `create_from_analysis_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'analysis_web_id' in params:
			if (params['analysis_web_id'] is not None):
				query_params['analysisWebId'] = params['analysis_web_id']
		if 'name' in params:
			if (params['name'] is not None):
				query_params['name'] = params['name']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/analysistemplates', 'POST',
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

		return self.api_client.call_api('/analysistemplates/{webId}', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIAnalysisTemplate',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update(self, web_id, template, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_with_http_info(web_id, template, **kwargs)
		else:
			(data) = self.update_with_http_info(web_id, template, **kwargs)
			return data

	def update_with_http_info(self, web_id, template, **kwargs):
		all_params = ['web_id', 'template']
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
		if ('template' not in params) or (params['template'] is None):
			raise ValueError("Missing the required parameter `template` when calling `update_with_http_info`")

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
		if 'template' in params:
			body_params = params['template']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/analysistemplates/{webId}', 'PATCH',
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

		return self.api_client.call_api('/analysistemplates/{webId}', 'DELETE',
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


	def get_categories(self, web_id, selected_fields, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_categories_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_categories_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_categories_with_http_info(self, web_id, selected_fields, web_id_type, **kwargs):
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
					" to method get_categories_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_categories_with_http_info`")

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

		return self.api_client.call_api('/analysistemplates/{webId}/categories', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsAnalysisCategory',
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

		return self.api_client.call_api('/analysistemplates/{webId}/security', 'GET',
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

		return self.api_client.call_api('/analysistemplates/{webId}/securityentries', 'GET',
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


	def create_security_entry(self, web_id, security_entry, apply_to_children, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_security_entry_with_http_info(web_id, security_entry, apply_to_children, web_id_type, **kwargs)
		else:
			(data) = self.create_security_entry_with_http_info(web_id, security_entry, apply_to_children, web_id_type, **kwargs)
			return data

	def create_security_entry_with_http_info(self, web_id, security_entry, apply_to_children, web_id_type, **kwargs):
		all_params = ['web_id', 'security_entry', 'apply_to_children', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_security_entry_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_security_entry_with_http_info`")
		if ('security_entry' not in params) or (params['security_entry'] is None):
			raise ValueError("Missing the required parameter `security_entry` when calling `create_security_entry_with_http_info`")

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
		if 'security_entry' in params:
			body_params = params['security_entry']
		if 'apply_to_children' in params:
			if (params['apply_to_children'] is not None):
				query_params['applyToChildren'] = params['apply_to_children']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/analysistemplates/{webId}/securityentries', 'POST',
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

		return self.api_client.call_api('/analysistemplates/{webId}/securityentries/{name}', 'GET',
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


	def update_security_entry(self, name, web_id, security_entry, apply_to_children, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_security_entry_with_http_info(name, web_id, security_entry, apply_to_children, **kwargs)
		else:
			(data) = self.update_security_entry_with_http_info(name, web_id, security_entry, apply_to_children, **kwargs)
			return data

	def update_security_entry_with_http_info(self, name, web_id, security_entry, apply_to_children, **kwargs):
		all_params = ['name', 'web_id', 'security_entry', 'apply_to_children']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method update_security_entry_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('name' not in params) or (params['name'] is None):
			raise ValueError("Missing the required parameter `name` when calling `update_security_entry_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `update_security_entry_with_http_info`")
		if ('security_entry' not in params) or (params['security_entry'] is None):
			raise ValueError("Missing the required parameter `security_entry` when calling `update_security_entry_with_http_info`")

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
		if 'security_entry' in params:
			body_params = params['security_entry']
		if 'apply_to_children' in params:
			if (params['apply_to_children'] is not None):
				query_params['applyToChildren'] = params['apply_to_children']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/analysistemplates/{webId}/securityentries/{name}', 'PUT',
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


	def delete_security_entry(self, name, web_id, apply_to_children, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.delete_security_entry_with_http_info(name, web_id, apply_to_children, **kwargs)
		else:
			(data) = self.delete_security_entry_with_http_info(name, web_id, apply_to_children, **kwargs)
			return data

	def delete_security_entry_with_http_info(self, name, web_id, apply_to_children, **kwargs):
		all_params = ['name', 'web_id', 'apply_to_children']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method delete_security_entry_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('name' not in params) or (params['name'] is None):
			raise ValueError("Missing the required parameter `name` when calling `delete_security_entry_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `delete_security_entry_with_http_info`")

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
		if 'apply_to_children' in params:
			if (params['apply_to_children'] is not None):
				query_params['applyToChildren'] = params['apply_to_children']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/analysistemplates/{webId}/securityentries/{name}', 'DELETE',
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


	def get_analysis_templates_query(self, database_web_id, max_count, query, selected_fields, start_index, web_id_type, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_analysis_templates_query_with_http_info(database_web_id, max_count, query, selected_fields, start_index, web_id_type, **kwargs)
		else:
			(data) = self.get_analysis_templates_query_with_http_info(database_web_id, max_count, query, selected_fields, start_index, web_id_type, **kwargs)
			return data

	def get_analysis_templates_query_with_http_info(self, database_web_id, max_count, query, selected_fields, start_index, web_id_type, **kwargs):
		all_params = ['database_web_id', 'max_count', 'query', 'selected_fields', 'start_index', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_analysis_templates_query_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']


		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'database_web_id' in params:
			if (params['database_web_id'] is not None):
				query_params['databaseWebId'] = params['database_web_id']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'query' in params:
			if (params['query'] is not None):
				query_params['query'] = params['query']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/analysistemplates/search', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsAnalysisTemplate',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)

