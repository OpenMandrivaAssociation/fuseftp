Name:		fuseftp
Summary:	FTP module for FUSE
Version:	0.8
Release:	11
License:	GPLv1 or Artistic
Group:		Development/Perl
URL:		https://github.com/marcust/fuseftp
Source0:	%{name}-%{version}.tar.bz2
Buildarch:	noarch
BuildRequires:	perl-devel
Requires:	fuse perl-Cache

%description
FTP module for FUSE.

%prep
%setup -q

%build
perl Makefile.PL INSTALLDIRS=vendor

%install
%makeinstall_std

%files
%doc README
%{_bindir}/%{name}


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.8-9mdv2011.0
+ Revision: 654374
- update file list
- rebuild for updated spec-helper

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-8mdv2011.0
+ Revision: 618374
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.8-7mdv2010.0
+ Revision: 428972
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.8-6mdv2009.0
+ Revision: 245508
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.8-4mdv2008.1
+ Revision: 151783
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.8-3mdv2008.1
+ Revision: 151782
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.8-2mdv2008.1
+ Revision: 125344
- kill re-definition of %%buildroot on Pixel's request
- import fuseftp


* Tue Apr 04 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.8-2mdk
- fix requires (fixes #21874)

* Fri Jan 06 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.8-1mdk
- Initial Mandriva release
