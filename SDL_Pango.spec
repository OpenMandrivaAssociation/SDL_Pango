%define name SDL_Pango
%define version 0.1.2
%define release %mkrel 2
%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}
%define _includedir %{_prefix}/include/SDL

Summary: Simple DirectMedia Layer for pango 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://puzzle.dl.sourceforge.net/sourceforge/sdlpango/%{name}-%{version}.tar.bz2
Patch0: SDL_Pango-0.1.2-API-adds.patch
License: LGPL
URL: http://sdlpango.sourceforge.net/
Group: System/Libraries
BuildRequires: libSDL-devel >= 1.2.4
BuildRequires: pango-devel >= 1.2.0

%description
Pango is the text rendering engine of GNOME 2.
SDL_Pango connects the engine to SDL.

%package -n %{lib_name}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name}
Obsoletes:	%{name}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{lib_name}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel
Obsoletes:	%{name}-devel

%description -n %{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/lib*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/*a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*



