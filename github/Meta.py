# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import github.GithubObject


class Meta(github.GithubObject.NonCompletableGithubObject):
    """
    Provides metadata about the github.com service. The reference can be found here http://developer.github.com/v3/meta/
    """

    @property
    def verifiable_password_authentication(self):
        return self._verifiable_password_authentication.value

    @property
    def github_services_sha(self):
        return self._github_services_sha.value

    @property
    def hooks(self):
        return self._hooks.value

    @property
    def git(self):
        return self._git.value

    @property
    def pages(self):
        return self._pages.value

    @property
    def importer(self):
        return self._importer.value

    def _initAttributes(self):
        self._verifiable_password_authentication = github.GithubObject.NotSet
        self._github_services_sha = github.GithubObject.NotSet
        self._hooks = github.GithubObject.NotSet
        self._git = github.GithubObject.NotSet
        self._pages = github.GithubObject.NotSet
        self._importer = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "verifiable_password_authentication" in attributes: # pragma no branch
            self._verifiable_password_authentication = self._makeBoolAttribute(attributes["verifiable_password_authentication"])
        if "github_services_sha" in attributes: # pragma no branch
            self._github_services_sha = self._makeStringAttribute(attributes["github_services_sha"])
        if "hooks" in attributes: # pragma no branch
            self._hooks = self._makeListOfStringsAttribute(attributes["hooks"])
        if "git" in attributes: # pragma no branch
            self._git = self._makeListOfStringsAttribute(attributes["git"])
        if "pages" in attributes: # pragma no branch
            self._pages = self._makeListOfStringsAttribute(attributes["pages"])
        if "importer" in attributes: # pragma no branch
            self._importer = self._makeListOfStringsAttribute(attributes["importer"])

