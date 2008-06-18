%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

%define _includedir %{_prefix}/include/SDL

Summary:	Simple DirectMedia Layer for pango 
Name:		SDL_Pango
Version:	0.1.2
Release:	%mkrel 6
License:	LGPLv2+
Group:		System/Libraries
URL:		http://sdlpango.sourceforge.net/
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/sdlpango/%{name}-%{version}.tar.bz2
Patch0:		SDL_Pango-0.1.2-API-adds.patch
BuildRequires:	libSDL-devel >= 1.2.4
BuildRequires:	pango-devel >= 1.2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Pango is the text rendering engine of GNOME 2.
SDL_Pango connects the engine to SDL.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name}
Obsoletes:	%{name}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}SDL_Pango1-devel < 0.1.2-4

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README
%{_libdir}/*a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
