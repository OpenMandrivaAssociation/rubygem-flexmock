%define	ruby_sitelib		%(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define	rubyabi	1.8

%define	gemdir		%(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define	gemname	flexmock
%define	geminstdir	%{gemdir}/gems/%{gemname}-%{version}

# Note
# 0.8.11 seems to work only with ruby 1.8.7+
# (test fails with 1.8.6.x (i.e. F-13))

Summary:	Mock object library for ruby
Name:		rubygem-%{gemname}
Version:	0.9.0
Release:	%mkrel 1
Group:		Development/Ruby 
License:	Copyright only
URL:		http://flexmock.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem

BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby-RubyGems
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(hoe)
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby-RubyGems
Provides:	rubygem(%{gemname}) = %{version}-%{release}
BuildArch:	noarch

%description
FlexMock is a simple, but flexible, mock object library for Ruby unit
testing.

%package	doc
Summary:	Documentation for %{name}
Group:		Development/Ruby 
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	-n ruby-%{gemname}
Summary:	Non-Gem support package for %{gemname}
Group:		Development/Ruby 
Requires:	%{name} = %{version}-%{release}
Provides:	ruby(%{gemname}) = %{version}-%{release}

%description    -n ruby-%{gemname}
This package provides non-Gem support for %{gemname}.

%prep
%setup -q -c -T

mkdir -p .%{gemdir}
gem install \
	--local \
	--install-dir .%{gemdir} \
	--force --rdoc -V \
	%{SOURCE0}

find . -name \*.rb | xargs sed -i -e '\@/usr/bin/env@d'
find . -name \*.gem -or -name \*.rb -or -name \*.rdoc | xargs chmod 0644

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/

# Create symlinks
# Copied from rubygem-getetxt.spec
##
## Note that before switching to gem %%{ruby_sitelib}/%%{gemname}
## already existed as a directory, so this cannot be replaced
## by symlink (cpio fails)
## Similarly, all directories under %%{ruby_sitelib} cannot be
## replaced by symlink
#

create_symlink_rec(){

ORIGBASEDIR=$1
TARGETBASEDIR=$2

## First calculate relative path of ORIGBASEDIR 
## from TARGETBASEDIR
TMPDIR=$TARGETBASEDIR
BACKDIR=
DOWNDIR=
num=0
nnum=0
while true
do
	num=$((num+1))
	TMPDIR=$(echo $TMPDIR | %{__sed} -e 's|/[^/][^/]*$||')
	DOWNDIR=$(echo $ORIGBASEDIR | %{__sed} -e "s|^$TMPDIR||")
	if [ x$DOWNDIR != x$ORIGBASEDIR ]
	then
		nnum=0
		while [ $nnum -lt $num ]
		do
			BACKDIR="../$BACKDIR"
			nnum=$((nnum+1))
		done
		break
	fi
done

RELBASEDIR=$( echo $BACKDIR/$DOWNDIR | %{__sed} -e 's|//*|/|g' )

## Next actually create symlink
pushd %{buildroot}/$ORIGBASEDIR
find . -type f | while read f
do
	DIRNAME=$(dirname $f)
	BACK2DIR=$(echo $DIRNAME | %{__sed} -e 's|/[^/][^/]*|/..|g')
	%{__mkdir_p} %{buildroot}${TARGETBASEDIR}/$DIRNAME
	LNNAME=$(echo $BACK2DIR/$RELBASEDIR/$f | \
		%{__sed} -e 's|^\./||' | %{__sed} -e 's|//|/|g' | \
		%{__sed} -e 's|/\./|/|' )
	%{__ln_s} -f $LNNAME %{buildroot}${TARGETBASEDIR}/$f
done
popd

}

create_symlink_rec %{geminstdir}/lib %{ruby_sitelib}

%check
pushd .%{geminstdir}
rake test_all --trace

%files
%defattr(-,root,root,-)
%dir	%{geminstdir}
%doc	%{geminstdir}/[A-Z]*
%{geminstdir}/lib/
%{geminstdir}/install.rb
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files	doc
%defattr(-,root,root,-)
%{geminstdir}/flexmock.blurb
%{geminstdir}/doc/
%{geminstdir}/test/
%{gemdir}/doc/%{gemname}-%{version}/

%files	-n ruby-%{gemname}
%defattr(-,root,root,-)
%{ruby_sitelib}/%{gemname}.rb
%{ruby_sitelib}/%{gemname}/
