Name:           perl-UNIVERSAL-isa
Version:        1.03
Release:        1%{?dist}
Summary:        Hack around module authors using UNIVERSAL::isa as a function

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/UNIVERSAL-isa/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/UNIVERSAL-isa-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Whenever you use "isa" in UNIVERSAL as a function, a kitten using
Test::MockObject dies. Normally, the kittens would be helpless, but
if they use UNIVERSAL::isa (the module whose docs you are reading),
the kittens can live long and prosper.

This module replaces UNIVERSAL::isa with a version that makes sure
that if it's called as a function on objects which override isa,
isa will be called on those objects as a method.

In all other cases the real UNIVERSAL::isa is just called directly.


%prep
%setup -q -n UNIVERSAL-isa-%{version}
%{__perl} -pi -e 's{^#!%{__perl}\b}{##!%{__perl}}' lib/UNIVERSAL/isa.pm


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*


%check
./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/*.3pm*


%changelog
* Wed Oct  7 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-1
- update to new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-1
- update to 1.01

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.06-5
- rebuild for new perl

* Wed Jan 02 2008 Ralf Corsépius <rc040203@freenet.de> - 0.06-4
- Update License-tag.

* Tue Dec 11 2007 Ralf Corsépius <rc040203@freenet.de> - 0.06-3
- Add BR: perl(Test::More).

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.06-2
- Rebuild for FC6.

* Fri Feb 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.06-1
- Update to 0.06.
- New files: Changes and README.

* Tue Jan 31 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-2
- Source URL correction.

* Tue Dec 27 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-1
- First build.
