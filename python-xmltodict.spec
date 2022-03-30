#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Make working with XML feel like you are working with JSON
Summary(pl.UTF-8):	Praca z XML działająca jak z JSON-em
Name:		python-xmltodict
Version:	0.12.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/xmltodict/
Source0:	https://files.pythonhosted.org/packages/source/x/xmltodict/xmltodict-%{version}.tar.gz
# Source0-md5:	ddb2bd078cef4f7e3021a578034ad941
URL:		https://pypi.org/project/xmltodict/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose >= 1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose >= 1.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmltodict is a Python module that makes working with XML feel like you
are working with JSON.

%description -l pl.UTF-8
xmltodict to moduł Pythona upodabniający pracę z XML-em do pracy z
JSON-em.

%package -n python3-xmltodict
Summary:	Make working with XML feel like you are working with JSON
Summary(pl.UTF-8):	Praca z XML działająca jak z JSON-em
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-xmltodict
xmltodict is a Python module that makes working with XML feel like you
are working with JSON.

%description -n python3-xmltodict -l pl.UTF-8
xmltodict to moduł Pythona upodabniający pracę z XML-em do pracy z
JSON-em.

%prep
%setup -q -n xmltodict-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/xmltodict.py[co]
%{py_sitescriptdir}/xmltodict-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-xmltodict
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/xmltodict.py
%{py3_sitescriptdir}/__pycache__/xmltodict.cpython-*.py[co]
%{py3_sitescriptdir}/xmltodict-%{version}-py*.egg-info
%endif
