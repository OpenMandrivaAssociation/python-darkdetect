%global pypi_name darkdetect 

Name:		python-%{pypi_name}
Version:	0.8.0
Release:	1
Summary:	Detect OS Dark Mode from Python 

Group:		Development/Python
License:	BSD
URL:		https://github.com/albertosottile/darkdetect
Source0:	https://files.pythonhosted.org/packages/source/d/darkdetect/darkdetect-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	git-core
BuildRequires:	python%{pyver}dist(setuptools)
#BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python

%description
This package allows to detect if the user is using Dark Mode on:

    macOS 10.14+
    Windows 10 1607+
    Linux with a dark GTK theme.

The main application of this package is to detect the Dark mode from your GUI Python application (Tkinter/wx/pyqt/qt for python (pyside)/...) 
and apply the needed adjustments to your interface. 
Darkdetect is particularly useful if your GUI library does not provide a public API for this detection (I am looking at you, Qt). 
In addition, this package does not depend on other modules or packages that are not already included in standard Python distributions.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%files
%license LICENSE
#{python3_sitelib}/%{pypi_name}*/
