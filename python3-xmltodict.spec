#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Make working with XML feel like you are working with JSON
Summary(pl.UTF-8):	Praca z XML działająca jak z JSON-em
Name:		python3-xmltodict
Version:	0.14.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/xmltodict/
Source0:	https://files.pythonhosted.org/packages/source/x/xmltodict/xmltodict-%{version}.tar.gz
# Source0-md5:	6e0d94bf858b3c2ff3daeed487eedc2a
URL:		https://pypi.org/project/xmltodict/
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
#BuildRequires:	
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmltodict is a Python module that makes working with XML feel like you
are working with JSON.

%description -l pl.UTF-8
xmltodict to moduł Pythona upodabniający pracę z XML-em do pracy z
JSON-em.

%prep
%setup -q -n xmltodict-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/xmltodict.py
%{py3_sitescriptdir}/__pycache__/xmltodict.cpython-*.py[co]
%{py3_sitescriptdir}/xmltodict-%{version}-py*.egg-info
