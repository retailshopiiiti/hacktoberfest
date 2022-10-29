%-------------------------
%  in Latex
% License : MIT
%------------------------

%---- Required Packages and Functions ----

\documentclass[a4paper,11pt]{article}
\usepackage{latexsym}
\usepackage{xcolor}
\usepackage{float}
\usepackage{ragged2e}
\usepackage[empty]{fullpage}
\usepackage{wrapfig}
\usepackage{lipsum}
\usepackage{tabularx}

\usepackage{algorithm}
\usepackage{algorithmic}

\usepackage{titlesec}
\usepackage{geometry}
\usepackage{marvosym}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{multicol}
\usepackage{graphicx}
\usepackage{cfr-lm}
\usepackage[T1]{fontenc}
\setlength{\multicolsep}{0pt} 
\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\geometry{left=1.4cm, top=0.8cm, right=1.2cm, bottom=1cm}
% Adjust margins
%\addtolength{\oddsidemargin}{-0.5in}
%\addtolength{\evensidemargin}{-0.5in}
%\addtolength{\textwidth}{1in}
\usepackage[most]{tcolorbox}
\tcbset{
	frame code={}
	center title,
	left=0pt,
	right=0pt,
	top=0pt,
	bottom=0pt,
	colback=gray!20,
	colframe=white,
	width=\dimexpr\textwidth\relax,
	enlarge left by=-2mm,
	boxsep=4pt,
	arc=0pt,outer arc=0pt,
}

\urlstyle{same}

\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-7pt}]

%-------------------------
% Custom commands
\newcommand{\resumeItem}[2]{
  \item{
    \textbf{#1}{:\hspace{0.5mm}#2 \vspace{-0.5mm}}
  }
}

\newcommand{\resumePOR}[3]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1},\hspace{0.3mm}#2 & \textit{\small{#3}} 
    \end{tabular*}
    \vspace{-2mm}
}

\newcommand{\resumeSubheading}[4]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1} & \textit{\footnotesize{#4}} \\
        \textit{\footnotesize{#3}} &  \footnotesize{#2}\\
    \end{tabular*}
    \vspace{-2.4mm}
}

\newcommand{\resumeProject}[4]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1} & \textit{\footnotesize{#3}} \\
        \footnotesize{\textit{#2}} & \footnotesize{#4}
    \end{tabular*}
    \vspace{-2.4mm}
}

\newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}\vspace{-4pt}}
% \renewcommand{\labelitemii}{$\circ$}
\renewcommand{\labelitemi}{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=*,labelsep=0mm]}
\newcommand{\resumeHeadingSkillStart}{\begin{itemize}[leftmargin=*,itemsep=1.7mm, rightmargin=2ex]}
\newcommand{\resumeItemListStart}{\begin{justify}\begin{itemize}[leftmargin=3ex, rightmargin=2ex, noitemsep,labelsep=1.2mm,itemsep=0mm]\small}

\newcommand{\resumeSubHeadingListEnd}{\end{itemize}\vspace{2mm}}
\newcommand{\resumeHeadingSkillEnd}{\end{itemize}\vspace{-2mm}}
\newcommand{\resumeItemListEnd}{\end{itemize}\end{justify}\vspace{-2mm}}
\newcommand{\cvsection}[1]{%
\vspace{2mm}
\begin{tcolorbox}
    \textbf{\large #1}
\end{tcolorbox}
    \vspace{-4mm}
}

\newcolumntype{L}{>{\raggedright\arraybackslash}X}%
\newcolumntype{R}{>{\raggedleft\arraybackslash}X}%
\newcolumntype{C}{>{\centering\arraybackslash}X}%
%---- End of Packages and Functions ------

%-------------------------------------------
%%%%%%  CV STARTS HERE  %%%%%%%%%%%
%%%%%% DEFINE ELEMENTS HERE %%%%%%%
\newcommand{\name}{Mayank Tayal} % Your Name
\newcommand{\course}{B.Tech - Computer Science and  Engineering} % Your Course
\newcommand{\roll}{200001043} % Your Roll No.
\newcommand{\phone}{7206637556} % Your Phone Number
\newcommand{\emaila}{cse200001043@iiti.ac.in} %Email 1
\newcommand{\emailb}{tayalmayank2000@gmail.com} %Email 2
\newcommand{\linkedin}{mayank-tayal-136b54211/} %linkedin




\begin{document}
\fontfamily{cmr}\selectfont
%----------HEADING-----------------



{
\begin{tabularx}{\linewidth}{L r}
  \textbf{\LARGE \name} 
  \\{Roll No.:\roll} & +91-\phone\\ 
  \course &  \href{mailto:\emaila}{\emaila}\\  
  {Indian Institute Of Technology Indore} & \href{mailto:\emailb}{\emailb}
  \\{} & \href{https://www.linkedin.com/in/\linkedin/}{\color{blue}linkedin.com/in/\linkedin}
\end{tabularx}
}



\vspace{-6mm}
\section{Education}

\setlength{\tabcolsep}{5pt} % Default value: 6pt
% \renewcommand{\arraystretch}{1.1} % Default value: 1
\small{\begin{tabularx}
{\dimexpr\textwidth-3mm\relax}{|c|C|c|c|}
  \hline
  \textbf{Degree/Certificate } & \textbf{Institute/Board} & \textbf{CGPA/Percentage} & \textbf{Year}\\
  \hline
  B.Tech. Major & Indian Institute of Technology Indore& 9.32 (Current) & 2020-Present\\

 %Optional
  \hline
  Senior Secondary & Modern Vidya Niketan / CBSE Board & 94.2\% & 2020 \\
  \hline
  Secondary & Dharam Public School / CBSE Board & 95.2\% & 2018 \\
  \hline
\end{tabularx}}
\vspace{-2mm}

%-----------EXPERIENCE-----------------
% \section{Experience}
%   \resumeSubHeadingListStart

%     \resumeSubheading
%       {XY Company Name}{Location}
%       {XXXXXXXXXXX \& YYYYYYYYYYYY Intern}{May 2019 - Jul. 2019}
%       \resumeItemListStart
%     \item {Work Done List 1}
%     \item {Work Done List 2}
%     % \item {More work done } .....
%     \resumeItemListEnd
    
%     % \resumeSubheading
%     %   {Company A}{Bengaluru, India}
%     %   {API Developer \& Machine Learning Intern}{May. 2018 - Jul. 2018}
%     %   \resumeItemListStart
%     % \item {XXXXXXXXXXXXXXX}
%     %     \item {YYYYYYYYYYYYYYYYYY}
%     % \resumeItemListEnd
      
%   \resumeSubHeadingListEnd
% \vspace{-5.5mm}
%-----------PROJECTS-----------------



% \section{Experience}
% \resumeSubHeadingListStart

%     \resumeProject
%       {Retail-IITI} %Project Name
%       {Prof- Dr. Nagendra kumar} %Project Name, Location Name
%       {Sep. 2021 - Oct. 2021} %Event Dates
%       {\href{https://github.com/cse200001043/RetailShop-IITI}{Github}} %Website
%       \resumeItemListStart
%         \item {A python website using Django framework }
%         \item {This is an e-shopping website where retailers can sell their projects and customers can buy them and helps user to track the order}
%     \resumeItemListEnd
    
 
      
%   \resumeSubHeadingListEnd
% \vspace{-5.5mm}


\section{Projects}
\resumeSubHeadingListStart

    \resumeProject
      {Online Examination System} %Project Name
      {Prof- Dr. Puneet Gupta} %Project Name, Location Name
      {Feb 2022 - Apr 2022} %Event Dates
      {\href{https://github.com/cse200001043/G6-P16-Online-Examination-System-1}{\color{blue}Github}} %Website
      \resumeItemListStart
        \item {A website using React library and Node.js environment and MongoDB used in backend }
        \item {This is an online examination website made under the Covid-19 scenario for conducting and grading online fair examinations and managing the university database}
    \resumeItemListEnd
    
    \resumeProject
      {RetailShop-IITI} %Project Name
      {Prof- Dr. Nagendra kumar} %Project Name, Location Name
      {Sep 2021 - Oct 2021} %Event Dates
      {\href{https://github.com/cse200001043/RetailShop-IITI}{\color{blue}Github}} %Website
      \resumeItemListStart
        \item {A python website using Django framework }
        \item {This is an e-shopping website where retailers can sell their projects and customers can buy them and helps user to track the order}
    \resumeItemListEnd
    
    
    \resumeProject
      {University-Database} %Project Name
      {Prof- Dr. Nagendra kumar} %Project Name, Location Name
      {Oct 2021 - Oct 2021} %Event Dates
      {\href{https://github.com/cse200001043/University-Database}{\color{blue}Github}} %Website
      \resumeItemListStart
        \item {A python website using Flask framework and MySQL}
        \item {This is a web application that handles the University Database to add and update lectures and assign students and professors to it}
    \resumeItemListEnd
    % \resumeItemListEnd
    
      
  \resumeSubHeadingListEnd
\vspace{-6mm}



\section{Technical Skills}
 \resumeHeadingSkillStart
  \resumeSubItem{Programming} % Category
    {C/C++, Python}
 \resumeSubItem{Tools/Frameworks} % Category
    {Python-Flask, Python-Django, Node.js, HTML/CSS, BootStrap,Mongoose,Github}
\resumeSubItem{Databases} % Category
    {MySQL, Sqlite} 
\resumeSubItem{Other Skills} % Category
    {Competitive Programming,Data Structures,Algorithms,Problem Solving and Team Management}
% \resumeSubItem{Devlopmen} % Category
%     {MySQL,MongoDB}
%  \resumeSubItem{Operating Systems}
%  {Windows, Linux*} 
\hfill \textit{\footnotesize{}} \hspace{3mm}
 \resumeHeadingSkillEnd


\section{Key courses taken}
\resumeHeadingSkillStart

% \resumeSubItem{Mathematics} % Category
%     {Linear Algebra, Basic Calculus \& Probability}
    

\resumeSubItem{Computer Science Course}
 {Discrete Mathematical Structures, Data Structures and Algorithms, Data Base & Information Systems, Design and Analysis of Algorithms, Software Engineering, Logic Design}

\resumeSubItem{Mathematics}
 {Calculus,Linear Algebra and Ordinary Differential Equation-I, Complex Analysis and Differential Equations-II, Numerical Methods}

%  \resumeSubItem{Data Structures and Algorithms} % Category
   
% \resumeSubItem{Full Stack Web Devlopment}
%  {Course Name 1, Course Name 2, Course Name 3, Course Name 4}
%  \resumeSubItem{Electrical and Electronics} % Category
%     {Advanced Control Systems, Digital Systems, Microprocessors} % Skills
 \resumeHeadingSkillEnd


% \section{Positions of Responsibility}
% \vspace{-0.4mm}
% \resumeSubHeadingListStart
% \resumePOR{Secretary} % Position
%     {XYZ Club, IIT Indore} %Club,Event
%     {Apr. 2018 - Apr. 2019} %Tenure Period
% \resumeSubHeadingListEnd
% \vspace{-4mm}


\section{Positions of Responsibility}
\vspace{-0.4mm}
\resumeSubHeadingListStart

\resumePOR{Writer and Tester} % Award
    {Divide By Zero, Division-2 contest on Codeforces} % Event
    {To be held in 2022} %Event Year

\resumePOR{Writer and Tester} % Award
    {Fool You 2022 Contest on Codechef} % Event
    {\href{https://www.codechef.com/FOYU2022}{\color{blue}15 Apr 2022}} %Event Year
    
\resumePOR{Tutor} % Award
    {Binary Brains, CP course by Prog Club} % Event
    {To be held in 2022} %Event Year
    
\resumePOR{Member} % Award
    {The Programming Club (CP Domain) IIT Indore } % Event
    {Aug 2021 - Present} %Event Year
    
% \resumePOR{Problem Setter and Tetser} % Award
%     {Divide By Zero 2022, Codeforces} % Event
%     {2022} %Event Year
    
\resumePOR{Member} % Award
    {Content and Publicity Team, Euristica’22 (IIT INDORE Programming Fest)} % Event
    {Apr 2022 - Jul 2022} %Event Year

\resumeSubHeadingListEnd
% \vspace{-2mm}
% \hfill \textit{\footnotesize{}} \hspace{3mm}
\vspace{-4mm}






\section{Achievements}
\vspace{-0.2mm}
\resumeSubHeadingListStart
    
\resumePOR{Max rating: 2101} % Award
    {Codeforces (Rated Master, Amongst top 100 in India)} % Event
    {\href{https://codeforces.com/profile/cse200001043}{\color{blue}cse200001043}} %Event Year
    
\resumePOR{Max rating: 2324} % Award
    {Codechef (Rated 6*, Amongst top 100 in India)} % Event
    {\href{https://www.codechef.com/users/tayalmayank}{\color{blue}tayalmayank}} %Event Year
    
\resumePOR{Max rating: 1587} % Award
    {Atcoder (Rated 3 Kyu, Amongst top 200 in India)} % Event
    {\href{https://codeforces.com/profile/cse200001043}{\color{blue}cse200001043}} %Event Year
    
    
\resumePOR{Gold Division} % Award
    {USACO } % Event
    {cse200001043} %Event Year
    
\resumePOR{90th rank} % Award
    {Weekly Contest 301, among 23500+ participants, Leetcode} % Event
    {\href{https://drive.google.com/file/d/1KS0gyEqyWA-O7DPfbUln7HKZPARStLyB/view?usp=sharing}{\color{blue}10 Jul 2022}} %Event Year

\resumePOR{144th rank} % Award
    {Newton's coding challenge August 2022, Newton School} % Event
    {\href{https://drive.google.com/file/d/19cMT_JA3VLuUIGZWJ-RSSKikSL1qH-Zy/view?usp=sharing}{\color{blue}31 August 2022}} %Event Year
    
\resumePOR{19th rank} % Award
    {Newton’s Grand Coding Contest 2022, Newton School} % Event
    {\href{https://drive.google.com/file/d/19cMT_JA3VLuUIGZWJ-RSSKikSL1qH-Zy/view?usp=sharing}{\color{blue}31 Mar 2022}} %Event Year
    
\resumePOR{AIR 3 (Global Rank - 74)} % Award
    {Codeforces Round 768, Div-2, among 17000+ participants} % Event
    {2022} %Event Year

\resumePOR{AIR 6 (Global Rank - 80)} % Award
    {Educational Codeforces Round 125, among 13500+ participants} % Event
    {2022} %Event Year
    
\resumePOR{324th rank (AIR -7)} % Award
    {Google CodeJam in Round 3} % Event
    {\href{https://drive.google.com/file/d/1BoBXJvfgJXq0G3xIkG3B10ST2j-PgwA8/view?usp=sharing}{\color{blue}4 Jun 2022}} %Event Year
    
\resumePOR{350th rank} % Award
    {Google Kick Start in Round A} % Event
    {\href{https://drive.google.com/file/d/1MFa_UVyFssReX13Fktkw0tKJz-VZhVoX/view?usp=sharing}{\color{blue}20 Mar 2022}}  %Event Year
    
\resumePOR{14th rank - 2 times, Inter IIT individual CP Contest} % Award
    {Inter IIT individual CP Contest } % Event
    {\href{https://drive.google.com/file/d/1XT42bjpRFU8sOfky_yUOn4iQI6fNEEL-/view?usp=sharing}{\color{blue}5 Feb 2022}} %Event Year
    
\resumePOR{3rd rank, Job-a-Thon 10:Hiring Challenge} % Award
    {among 10,000+ Participants, GeeksforGeeks} % Event
    {\href{https://drive.google.com/file/d/1OpJp0Zqrl5F_0pSUfoZh-SZ3U41ivJWK/view?usp=sharing}{\color{blue}21 Jul 2022}} %Event Year
    
\resumePOR{3rd Rank} % Award
    {Codedrift July 2.0, Interviewbit} % Event
    {\href{https://moonshot.scaler.com/s/sl/6kpJf89P0_}{\color{blue}23 Jul 2022}} %Event Year
    
\resumePOR{8th Rank} % Award
    {CodeDrift August 2.0, Interviewbit} % Event
    {\href{https://moonshot.scaler.com/s/sl/6kpJf89P0_}{\color{blue}23 Jul 2022}} %Event Year
    
\resumePOR{4th Rank} % Award
    {Codedrift September 1.0, Interviewbit} % Event
    {\href{https://moonshot.scaler.com/s/sl/6kpJf89P0_}{\color{blue}23 Jul 2022}} %Event Year
    
% \resumePOR{Inter IIT individual CP Contest} % Award
%     {Secured 8th rank} % Event
%     {2022} %Event Year
    
\resumePOR{1500+ problems solved} % Award
    {related to DSA and CP(750+ on CF and rest on other sites)} % Event
    {\href{https://codeforces.com/profile/cse200001043}{\color{blue}cse200001043}} %Event Year

\resumePOR{47th rank (AIR - 4)} % Award
    {Google Kick Start in Round F} % Event
    {\href{https://drive.google.com/file/d/1MFa_UVyFssReX13Fktkw0tKJz-VZhVoX/view?usp=sharing}{\color{blue}20 Mar 2022}}  %Event Year
    
\resumePOR{31th rank} % Award
    {Google Kick Start in Round G} % Event
    {\href{https://drive.google.com/file/d/1MFa_UVyFssReX13Fktkw0tKJz-VZhVoX/view?usp=sharing}{\color{blue}20 Mar 2022}}  %Event Year
    
\resumePOR{8th rank} % Award
    {ICPC Kanpur Preliminary 2021} % Event
    {\href{https://drive.google.com/file/d/19cMT_JA3VLuUIGZWJ-RSSKikSL1qH-Zy/view?usp=sharing}{\color{blue}31 August 2022}} %Event Year
    
\resumePOR{10th rank} % Award
    {ICPC Kanpur Regional 2021} % Event
    {\href{https://drive.google.com/file/d/19cMT_JA3VLuUIGZWJ-RSSKikSL1qH-Zy/view?usp=sharing}{\color{blue}31 August 2022}} %Event Year
    
\resumePOR{16th rank} % Award
    {ICPC Amritapuri Preliminary 2021} % Event
    {\href{https://drive.google.com/file/d/19cMT_JA3VLuUIGZWJ-RSSKikSL1qH-Zy/view?usp=sharing}{\color{blue}31 August 2022}} %Event Year

\resumePOR{26th rank} % Award
    {ICPC Amritapuri Regional 2021} % Event
    {\href{https://drive.google.com/file/d/19cMT_JA3VLuUIGZWJ-RSSKikSL1qH-Zy/view?usp=sharing}{\color{blue}31 August 2022}} %Event Year
    
\resumeSubHeadingListEnd
% \vspace{-2mm}
% \hfill \textit{\footnotesize{}} \hspace{3mm}
\vspace{-3mm}
% \section{Summary}
% \begin{algorithmic}
% \STATE As a student as well as a person, I am a person who likes to get things done on time. I always put in the highest amount of effort and sincerity into everything I do. My interests mainly lie in programming and Full-Stack Development. I pursue cp on various coding platforms (mainly codeforces).
% \end{algorithmic}
% \vspace{-3.5mm}
\hspace*{0mm}\rule{1.0\textwidth}{0.1mm}

%-------------------------------------------
\end{document}
