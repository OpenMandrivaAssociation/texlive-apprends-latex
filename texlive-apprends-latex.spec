Name:		texlive-apprends-latex
Version:	19306
Release:	1
Summary:	Apprends LaTeX!
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/apprends-latex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apprends-latex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apprends-latex.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
