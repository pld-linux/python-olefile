#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 module to parse, read and write Microsoft OLE2 files
Summary(pl.UTF-8):	Moduł Pythona 2 do analizy, odczytu i zapisu plików Microsoft OLE2
Name:		python-olefile
Version:	0.46
Release:	7
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/olefile/
Source0:	https://files.pythonhosted.org/packages/source/o/olefile/olefile-%{version}.zip
# Source0-md5:	af351575e53aa00c36ae1c71ee9b0043
URL:		https://pypi.org/project/olefile
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	sed >= 4.0
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 package to parse, read and write Microsoft OLE2 files (also
called Structured Storage, Compound File Binary Format or Compound
Document File Format), such as Microsoft Office 97-2003 documents,
vbaProject.bin in MS Office 2007+ files, Image Composer and FlashPix
files, Outlook messages, StickyNotes, several Microscopy file formats,
McAfee antivirus quarantine files, etc.

%description -l pl.UTF-8
Pakiet Pythona 2 do analizy, odczytu i zapisu plików Microsoft OLE2
(znanych też jako Structured Storage, Compound File Binary Format albo
Compound Document File Format), takich jak dokumenty Microsoft Office
97-2003, vbaProject.bin w plikach MS Office 2007+, pliki Image
Composera i FlashPix, wiadomości Outlooka, StickyNotes, różne formaty
plików Microscopy, pliki kwarantanny antywirusa McAfee itp.

%package -n python3-olefile
Summary:	Python 3 module to parse, read and write Microsoft OLE2 files
Summary(pl.UTF-8):	Moduł Pythona 3 do analizy, odczytu i zapisu plików Microsoft OLE2
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-olefile
Python 3 package to parse, read and write Microsoft OLE2 files (also
called Structured Storage, Compound File Binary Format or Compound
Document File Format), such as Microsoft Office 97-2003 documents,
vbaProject.bin in MS Office 2007+ files, Image Composer and FlashPix
files, Outlook messages, StickyNotes, several Microscopy file formats,
McAfee antivirus quarantine files, etc.

%description -n python3-olefile -l pl.UTF-8
Pakiet Pythona 3 do analizy, odczytu i zapisu plików Microsoft OLE2
(znanych też jako Structured Storage, Compound File Binary Format albo
Compound Document File Format), takich jak dokumenty Microsoft Office
97-2003, vbaProject.bin w plikach MS Office 2007+, pliki Image
Composera i FlashPix, wiadomości Outlooka, StickyNotes, różne formaty
plików Microscopy, pliki kwarantanny antywirusa McAfee itp.

%package apidocs
Summary:	API documentation for Python olefile module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona olefile
Group:		Documentation

%description apidocs
API documentation for Pythona olefile module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona olefile.

%prep
%setup -q -n olefile-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} tests/test_olefile.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-3/lib \
%{__python3} tests/test_olefile.py
%endif
%endif

%if %{with doc}
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-3
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
%doc CONTRIBUTORS.txt LICENSE.txt README.md
%{py_sitescriptdir}/olefile
%{py_sitescriptdir}/olefile-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-olefile
%defattr(644,root,root,755)
%doc CONTRIBUTORS.txt LICENSE.txt README.md
%{py3_sitescriptdir}/olefile
%{py3_sitescriptdir}/olefile-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_images,_static,*.html,*.js}
%endif
