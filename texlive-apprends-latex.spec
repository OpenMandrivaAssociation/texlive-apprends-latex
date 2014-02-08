# revision 19306
# category Package
# catalog-ctan /info/apprends-latex
# catalog-date 2010-07-09 10:38:38 +0200
# catalog-license lppl
# catalog-version 4.02
Name:		texlive-apprends-latex
Version:	4.02
Release:	3
Summary:	Apprends LaTeX!
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/apprends-latex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apprends-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apprends-latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Apprends LaTeX! ("Learn LaTeX", in English) is French
documentation for LaTeX beginners.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/apprends-latex/Apprends_LaTeX.pdf
%doc %{_texmfdistdir}/doc/latex/apprends-latex/Apprends_LaTeX.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/README
%doc %{_texmfdistdir}/doc/latex/apprends-latex/avance.bib
%doc %{_texmfdistdir}/doc/latex/apprends-latex/bibliographie-index.bib
%doc %{_texmfdistdir}/doc/latex/apprends-latex/divers.bib
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/Makefile
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/beamer-themes.pl
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/beamer-titlepage.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/currvita.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/curve-experience.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/curve-extra.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/curve-formation.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/curve-langues.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/curve-methodologies.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/curve-references.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/curve.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/letter.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/moderncv.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/polices.pl
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/scrlttr2.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/seraphin-lampion.jpg
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/slides.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/exemples/tikz.tex
%doc %{_texmfdistdir}/doc/latex/apprends-latex/graphisme.bib
%doc %{_texmfdistdir}/doc/latex/apprends-latex/index.ist
%doc %{_texmfdistdir}/doc/latex/apprends-latex/latex.bib
%doc %{_texmfdistdir}/doc/latex/apprends-latex/latexmkrc
%doc %{_texmfdistdir}/doc/latex/apprends-latex/typographie.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.02-2
+ Revision: 749288
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.02-1
+ Revision: 717845
- texlive-apprends-latex
- texlive-apprends-latex
- texlive-apprends-latex
- texlive-apprends-latex

