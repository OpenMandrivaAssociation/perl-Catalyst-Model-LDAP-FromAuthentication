%define upstream_name    Catalyst-Model-LDAP-FromAuthentication
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Provides an LDAP model bound as the user who logged in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
# Get 0.01, which is not on CPAN, at:
# http://github.com/bobtfish/catalyst-model-ldap-fromauthentication/tarball/0.01
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Authentication::Store::LDAP)
BuildRequires:	perl(Catalyst::Component::InstancePerContext)
BuildRequires:	perl(Catalyst::Model::LDAP)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types::Common::String)
BuildRequires:	perl(MooseX::Types::LoadableClass)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Module::CoreList)
BuildArch:	noarch

%description
Provides an LDAP model bound as the user who logged in.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 's/^(use Module::Install::Author)/#$1/g;s/^(author_)/#$1/g' Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 656887
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 602139
- new version

  + Buchan Milne <bgmilne@mandriva.org>
    - BR Module::CoreList for 2010.0

* Tue Oct 12 2010 Buchan Milne <bgmilne@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 585120
- Fix buildrequires
- import perl-Catalyst-Model-LDAP-FromAuthentication

