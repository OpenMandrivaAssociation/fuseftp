%define	name	fuseftp
%define	version	0.8
%define	release	%mkrel 7

Name:		%{name}
Summary:	FTP module for FUSE
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://wiki.thiesen.org/page/Fuseftp
Source0:	%{name}-%{version}.tar.bz2
Buildarch:	noarch
Requires:	fuse perl-Cache
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
FTP module for FUSE.

%prep
%setup -q

%build
perl Makefile.PL INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/auto/%{name}
%{_bindir}/%{name}

