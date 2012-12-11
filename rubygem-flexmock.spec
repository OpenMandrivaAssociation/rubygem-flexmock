# Generated from flexmock-0.9.0.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	flexmock

Summary:	Simple and Flexible Mock Objects for Testing
Name:		rubygem-%{rbname}

Version:	1.0.3
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/jimweirich/flexmock
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch
%rename		ruby-flexmock

%description
FlexMock is a extremely simple mock object class compatible
with the Test::Unit framework.  Although the FlexMock's
interface is simple, it is very flexible.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/examples/*.rdoc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/flexmock
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/flexmock/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/flexmock/rails
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/flexmock/rails/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test/rspec_integration
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/rspec_integration/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test/test_unit_integration
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/test_unit_integration/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGES
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/*.rdoc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/releases
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/releases/*.rdoc


%changelog
* Fri Feb 17 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.0-3
+ Revision: 775597
- %rename ruby-flexmock

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.0-2
+ Revision: 774534
- regenerate spec with gem2rpm5
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Sep 12 2011 Alexander Barakin <abarakin@mandriva.org> 0.9.0-1
+ Revision: 699539
- missing rdoc fix
- imported package rubygem-flexmock

* Fri Dec 03 2010 Rémy Clouard <shikamaru@mandriva.org> 0.8.11-1mdv2011.0
+ Revision: 606980
- import rubygem-flexmock

