Name:		python-pyotp
Version:	2.9.0
Release:	1
Source0:	https://github.com/pyauth/pyotp/archive/refs/tags/v%{version}.tar.gz
Summary:	Python One Time Password Library
URL:		https://pypi.org/project/pyotp/
License:	MIT License
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python One Time Password Library

%files
%{py_sitedir}/pyotp
%{py_sitedir}/pyotp-*.*-info
