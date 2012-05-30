Name:           diffutils
Version:        3.0
Release:        1
License:        GPLv2+
Summary:        A GNU collection of diff utilities
Url:            http://www.gnu.org/software/diffutils/diffutils.html
Group:          Applications/Text
Source:         ftp://ftp.gnu.org/gnu/diffutils/diffutils-%{version}.tar.xz
Source1001: packaging/diffutils.manifest 
Patch0:         diffutils-cmp-s-empty.patch

%description
Diffutils includes four utilities: diff, cmp, diff3 and sdiff. Diff
compares two files and shows the differences, line by line.  The cmp
command shows the offset and line numbers where two files differ, or
cmp can show the characters that differ between the two files.  The
diff3 command shows the differences between three files.  Diff3 can be
used when two people have made independent changes to a common
original; diff3 can produce a merged file that contains both sets of
changes and warnings about conflicts.  The sdiff command can be used
to merge two files interactively.

Install diffutils if you need to compare text files.

%prep
%setup -q
%patch0 -p1 

%build
cp %{SOURCE1001} .
%configure --disable-nls
make PR_PROGRAM=%{_bindir}/pr

%install
%make_install

%clean
rm -rf %{buildroot}

%docs_package 

%files 
%manifest diffutils.manifest
%defattr(-,root,root,-)
%doc NEWS README COPYING
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/diff.info*gz
