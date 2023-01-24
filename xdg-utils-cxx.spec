Name:		xdg-utils-cxx
Version:	1.0.1
Release:	1
Summary:	Implementation of the FreeDesktop specifications to be used in C++ projects
Group:		Development/C++
License:	MIT
Url:		https://github.com/azubieta/xdg-utils-cxx
Source0:	https://github.com/azubieta/xdg-utils-cxx/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
BuildRequires:	cmake

%description
Implementation of the Free Desktop Standards in C++.
This project was started to fulfill the need of a reliable implementations 
of such standards in the AppImage project. It is totally standalone and only 
depends on the standard c++ libraries (stdlib).

%files
%{_includedir}/XdgUtils
%{_libdir}/XdgUtils
%{_libdir}/cmake/XdgUtils

#------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake
%make

%install
%makeinstall_std -C build
