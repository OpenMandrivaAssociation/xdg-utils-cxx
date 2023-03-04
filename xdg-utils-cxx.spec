%define _empty_manifest_terminate_build 0

Name:		xdg-utils-cxx
Version:	1.0.1
Release:	3
Summary:	Implementation of the FreeDesktop specifications to be used in C++ projects
Group:		Development/C++
License:	MIT
Url:		https://github.com/azubieta/xdg-utils-cxx
Source0:	https://github.com/azubieta/xdg-utils-cxx/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:   fix_so_version.patch
Patch1:   fix_install_path.patch
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
%cmake \
        -DXDG_UTILS_SHARED=ON \
        -DXDG_UTILS_TESTS=OFF
%make_build

%install
%make_install -C build
