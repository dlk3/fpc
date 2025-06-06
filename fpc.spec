%define  debug_package %{nil}

Name:		fpc
Version:	3.2.4
Release:	3
Summary:	Free Pascal Compiler
License:	GPLv2+ and LGPLv2+ with exceptions # https://wiki.lazarus.freepascal.org/FPC_modified_LGPL
URL:		https://www.freepascal.org
Source0:	%{name}-%{version}.tar.gz
BuildArch:	x86_64

BuildRequires:	fpc == 3.2.2
BuildRequires: 	glibc-devel
BuildRequires:	qt5pas-devel
BuildRequires:  libX11-devel

%description
An updated, development version of the Free Pascal Compiler, intended only to
be used in the COPR build environment for building lighterowl's transgui 
package.  Do not install this on your workstation, it will break stuff.

%prep
%setup -q

%build
make all

%install
make PREFIX=%{buildroot}/usr install
cd %{buildroot}
mv usr/lib usr/lib64
mkdir etc
usr/lib64/%{name}/%{version}/samplecfg /usr/lib64/${name}/%{version} etc

%files
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/libpas2jslib.so*
%config(noreplace) %{_sysconfdir}/*
%dir %{_defaultdocdir}/%{name}-%{version}/
%doc %{_defaultdocdir}/%{name}-%{version}/*

%changelog
* Thu Jun 05 2025 dlk3 <dave@daveking.com> 3.2.4-3
- Test removing --nowait option from COPR build process (dave@daveking.com)

* Thu Jun 05 2025 dlk3 <dave@daveking.com> 3.2.4-2
- Developing spec file to work with tito build (dave@daveking.com)
