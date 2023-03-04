%define _empty_manifest_terminate_build 0

%define libname %mklibname xdg-utils-cxx %{api} %{major}
%define devname %mklibname -d xdg-utils-cxx %{api}

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

%package -n %{libname}
Summary:        Shared library for %{name}
Provides:       xdg-utils-cxx

%description -n %{libname}
Library for implementation of the FreeDesktop specifications to be used in C++ projects

%files -n %{libname}
%{_libdir}/libXdgUtilsBaseDir.so.1.0.1
%{_libdir}/libXdgUtilsDesktopEntry.so.1.0.1

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Privides:       xdg-utils-cxx-devel

%description -n %{devname}
Development files for implementation of the FreeDesktop specifications to be used in C++ projects

%files -n %{devname}
%{_includedir}/XdgUtils
%{_libdir}/libXdgUtilsBaseDir.so
%{_libdir}/libXdgUtilsDesktopEntry.so
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
