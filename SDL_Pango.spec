%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

%define _includedir %{_prefix}/include/SDL

Summary:	Simple DirectMedia Layer for pango
Name:		SDL_Pango
Version:	0.1.2
Release:	12
License:	LGPLv2+
Group:		System/Libraries
URL:		http://sdlpango.sourceforge.net/
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/sdlpango/%{name}-%{version}.tar.bz2
Patch0:		SDL_Pango-0.1.2-API-adds.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangoft2)

%description
Pango is the text rendering engine of GNOME 2.
SDL_Pango connects the engine to SDL.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc README
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-9mdv2011.0
+ Revision: 671968
- mass rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-8mdv2011.0
+ Revision: 520005
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-7mdv2010.0
+ Revision: 413007
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-6mdv2009.0
+ Revision: 225430
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-5mdv2008.1
+ Revision: 151075
- fix obsolete

* Sun Jan 13 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-4mdv2008.1
+ Revision: 151074
- provide %%name-devel
- versionize obsoletes
- do not provide old -devel name

* Sun Jan 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-3mdv2008.1
+ Revision: 150943
- new license policy
- new devel policy
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 23 2007 Michael Scherer <misc@mandriva.org> 0.1.2-2mdv2008.0
+ Revision: 29965
- rebuild for new directfb and SDL


* Sat Oct 28 2006 Michael Scherer <misc@mandriva.org> 0.1.2-1mdv2007.0
+ Revision: 73540
- add missing pango-devel
- Import SDL_Pango

