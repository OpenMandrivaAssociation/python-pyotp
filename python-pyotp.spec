%define oname   pyotp

Name:           python-pyotp
Version:        2.10.0
Release:        2
Source0:        https://files.pythonhosted.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
Summary:        Python One Time Password Library
URL:            https://pypi.org/project/pyotp/
License:        MIT License
Group:          Development/Python
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(hatch-vcs)
BuildSystem:    python
BuildArch:      noarch

%description
Python One Time Password Library

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-*.*-info
