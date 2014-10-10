%define	upstream_name	 BFD
%define	upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Impromptu dumping of data structures for debugging purposes  
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Allows for impromptu dumping of output to STDERR. Useful when you want to take
a peek at a nest Perl data structure by emitting (relatively) nicely formatted
output with filename and line number prefixed to each line.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/BFD.pm
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 680657
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 504586
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.31-7mdv2010.0
+ Revision: 430265
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.31-6mdv2009.0
+ Revision: 255400
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.31-4mdv2008.1
+ Revision: 131173
- kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.31-4mdv2007.0
+ Revision: 73330
- import perl-BFD-0.31-4mdv2007.0

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-4mdv2007.0
- Rebuild

* Thu Feb 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-3mdk
- spec cleanup
- fix directory ownership
- %%{1}mdv2007.1
- better description and url

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.31-2mdk
- rebuild for new perl

* Thu Apr 29 2004 Michael Scherer <misc@mandrake.org> 0.31-1mdk 
- first version

