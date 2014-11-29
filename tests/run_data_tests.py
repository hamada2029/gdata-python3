#!/usr/bin/python

import sys
import unittest
from . import module_test_runner
import getopt
import getpass
# Modules whose tests we will run.
from . import gdata_test
from . import atom_test
from . import atom_tests.http_interface_test
from . import atom_tests.mock_http_test
from . import atom_tests.token_store_test
from . import atom_tests.url_test
from . import atom_tests.core_test
from . import gdata_tests.apps.emailsettings.data_test
from . import gdata_tests.apps.multidomain.data_test
from . import gdata_tests.apps_test
from . import gdata_tests.auth_test
from . import gdata_tests.books_test
from . import gdata_tests.blogger_test
from . import gdata_tests.calendar_test
from . import gdata_tests.calendar_resource.data_test
from . import gdata_tests.client_test
from . import gdata_tests.codesearch_test
from . import gdata_tests.contacts_test
from . import gdata_tests.docs_test
from . import gdata_tests.health_test
from . import gdata_tests.photos_test
from . import gdata_tests.spreadsheet_test
from . import gdata_tests.youtube_test
from . import gdata_tests.webmastertools_test
from . import gdata_tests.oauth.data_test


def RunAllTests():
  test_runner = module_test_runner.ModuleTestRunner()
  test_runner.modules = [gdata_test, atom_test, atom_tests.url_test, 
                         atom_tests.http_interface_test, 
                         atom_tests.mock_http_test, 
                         atom_tests.core_test,
                         atom_tests.token_store_test,
                         gdata_tests.client_test,
                         gdata_tests.apps_test,
                         gdata_tests.apps.emailsettings.data_test,
                         gdata_tests.apps.multidomain.data_test,
                         gdata_tests.auth_test, 
                         gdata_tests.books_test,
                         gdata_tests.calendar_test, gdata_tests.docs_test,
                         gdata_tests.health_test, gdata_tests.spreadsheet_test,
                         gdata_tests.photos_test, gdata_tests.codesearch_test,
                         gdata_tests.contacts_test,
                         gdata_tests.youtube_test, gdata_tests.blogger_test, 
                         gdata_tests.webmastertools_test,
                         gdata_tests.calendar_resource.data_test,
                         gdata_tests.oauth.data_test]
  test_runner.RunAllTests()
  
if __name__ == '__main__':
  RunAllTests()
