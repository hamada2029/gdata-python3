#!/usr/bin/python3
#
# Copyright 2011 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Data model tests for the Organization Unit Provisioning API."""


__author__ = 'Gunjan Sharma <gunjansharma@google.com>'


import unittest
import atom.core
from gdata import test_data
import gdata.apps.organization.data
import gdata.test_config as conf


class CustomerIdEntryTest(unittest.TestCase):

  def setUp(self):
    self.entry = atom.core.parse(test_data.ORGANIZATION_UNIT_CUSTOMER_ID_ENTRY,
                                 gdata.apps.organization.data.CustomerIdEntry)

  def testCustomerIdEntryFromString(self):
    self.assertTrue(isinstance(self.entry,
                            gdata.apps.organization.data.CustomerIdEntry))
    self.assertEqual(self.entry.customer_id, 'C123A456B')
    self.assertEqual(self.entry.customer_org_unit_name, 'example.com')
    self.assertEqual(self.entry.customer_org_unit_description, 'example.com')
    self.assertEqual(self.entry.org_unit_name, 'example.com')
    self.assertEqual(self.entry.org_unit_description, 'tempdescription')


class OrgUnitEntryTest(unittest.TestCase):

  def setUp(self):
    self.entry = atom.core.parse(test_data.ORGANIZATION_UNIT_ORGUNIT_ENTRY,
                                 gdata.apps.organization.data.OrgUnitEntry)
    self.feed = atom.core.parse(test_data.ORGANIZATION_UNIT_ORGUNIT_FEED,
                                gdata.apps.organization.data.OrgUnitFeed)

  def testOrgUnitEntryFromString(self):
    self.assertTrue(isinstance(self.entry,
                            gdata.apps.organization.data.OrgUnitEntry))
    self.assertEqual(self.entry.org_unit_description, 'New Test Org')
    self.assertEqual(self.entry.org_unit_name, 'Test Organization')
    self.assertEqual(self.entry.org_unit_path, 'Test/Test+Organization')
    self.assertEqual(self.entry.parent_org_unit_path, 'Test')
    self.assertEqual(self.entry.org_unit_block_inheritance, 'false')

  def testOrgUnitFeedFromString(self):
    self.assertEqual(len(self.feed.entry), 2)
    self.assertTrue(isinstance(self.feed,
                            gdata.apps.organization.data.OrgUnitFeed))
    self.assertTrue(isinstance(self.feed.entry[0],
                            gdata.apps.organization.data.OrgUnitEntry))
    self.assertTrue(isinstance(self.feed.entry[1],
                            gdata.apps.organization.data.OrgUnitEntry))
    self.assertEqual(
        self.feed.entry[0].find_edit_link(),
        ('https://apps-apis.google.com/a/feeds/orgunit/2.0/'
         'C123A456B/testOrgUnit92'))
    self.assertEqual(self.feed.entry[0].org_unit_description, 'test92')
    self.assertEqual(self.feed.entry[0].org_unit_name, 'testOrgUnit92')
    self.assertEqual(self.feed.entry[0].org_unit_path, 'Test/testOrgUnit92')
    self.assertEqual(self.feed.entry[0].parent_org_unit_path, 'Test')
    self.assertEqual(self.feed.entry[0].org_unit_block_inheritance, 'false')
    self.assertEqual(
        self.feed.entry[1].find_edit_link(),
        ('https://apps-apis.google.com/a/feeds/orgunit/2.0/'
         'C123A456B/testOrgUnit93'))
    self.assertEqual(self.feed.entry[1].org_unit_description, 'test93')
    self.assertEqual(self.feed.entry[1].org_unit_name, 'testOrgUnit93')
    self.assertEqual(self.feed.entry[1].org_unit_path, 'Test/testOrgUnit93')
    self.assertEqual(self.feed.entry[1].parent_org_unit_path, 'Test')
    self.assertEqual(self.feed.entry[1].org_unit_block_inheritance, 'false')


class OrgUserEntryTest(unittest.TestCase):

  def setUp(self):
    self.entry = atom.core.parse(test_data.ORGANIZATION_UNIT_ORGUSER_ENTRY,
                                 gdata.apps.organization.data.OrgUserEntry)
    self.feed = atom.core.parse(test_data.ORGANIZATION_UNIT_ORGUSER_FEED,
                                gdata.apps.organization.data.OrgUserFeed)

  def testOrgUserEntryFromString(self):
    self.assertTrue(isinstance(self.entry,
                            gdata.apps.organization.data.OrgUserEntry))
    self.assertEqual(self.entry.user_email, 'admin@example.com')
    self.assertEqual(self.entry.org_unit_path, 'Test')

  def testOrgUserFeedFromString(self):
    self.assertEqual(len(self.feed.entry), 2)
    self.assertTrue(isinstance(self.feed,
                            gdata.apps.organization.data.OrgUserFeed))
    self.assertTrue(isinstance(self.feed.entry[0],
                            gdata.apps.organization.data.OrgUserEntry))
    self.assertTrue(isinstance(self.feed.entry[1],
                            gdata.apps.organization.data.OrgUserEntry))
    self.assertEqual(
        self.feed.entry[0].find_edit_link(),
        ('https://apps-apis.google.com/a/feeds/orguser/2.0/'
         'C123A456B/user720430%40example.com'))
    self.assertEqual(self.feed.entry[0].user_email, 'user720430@example.com')
    self.assertEqual(self.feed.entry[0].org_unit_path, 'Test')
    self.assertEqual(
        self.feed.entry[1].find_edit_link(),
        ('https://apps-apis.google.com/a/feeds/orguser/2.0/'
         'C123A456B/user832648%40example.com'))
    self.assertEqual(self.feed.entry[1].user_email, 'user832648@example.com')
    self.assertEqual(self.feed.entry[1].org_unit_path, 'Test')


def suite():
  return conf.build_suite([OrgUnitEntryTest, OrgUserEntryTest])


if __name__ == '__main__':
  unittest.main()
