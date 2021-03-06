URL = """
http://Docs.opencv.org/doc/user_guide/ug_traincascade.html.
www.it-ebooks.info.
https://mail.google.com
"""
tURL ="""
http___Docs_opencv_org_doc_user_guide_ug_traincascade_html.
www_it_ebooks_info.
https___mail_google_com
"""

#Note: this sequence contain \t white spaces
DOT_SEQUENCE = """
For other (optional) flags of <opencv_createsamples>, see the official... documentation
4 Después. . . 
2.	 Learn advanced.. .	. web2py usage from building
....................
"""

rDOT_SEQUENCE = """
For other (optional) flags of <opencv_createsamples>, see the official    documentation
4 Después    . 
2.	 Learn advanced    	  web2py usage from building
                    
"""

MULTIPART_WORDS = """
www.it-ebooks.info.
Over 110 recipes to master this full-stack Python web
ISBN: 978-1-78216-162-2
Ahora probaremos la división al final de ca-
–Reunieronse pues Lic., Dr., Ing., Ph.D. y todos los que de una for-
"""

rMWORDS = """
www_it_ebooks_info.
Over 110 recipes to master this full_stack Python web
ISBN: 978_1_78216_162_2
Ahora probaremos la división al final de ca-
–Reunieronse pues Lic., Dr., Ing., Ph_D. y todos los que de una for-
"""

ABBR = """
A.D.  "Ante diem",
A.D.V. Ante diem quintum.",
 A.D.A. :  "Ad dandos agros ANN.
ANN. :  "Annales, Anni, Annona."

"Ap. Sed. Leg.":  "Apostolicæ Sedis Legatus"
"Bon. Mem.":  "Bonæ Memoriæ"
GNU is a project
M. Douglas is not a valid name
"""

eABBR = """
Ante diem  "Ante diem",
A.D.V. Ante diem quintum.",
 Ad dandos agros. :  "Ad dandos agros ANN.
Annales, Anni, Annona. :  "Annales, Anni, Annona."

"Apostolicæ Sedis Legatus (Legate of the Apostolic See)":  "Apostolicæ Sedis Legatus"
"Bonæ Memoriæ (Of Happy Memory)":  "Bonæ Memoriæ"
GNU is Not Unix is a project
M. Douglas is not a valid name
"""

ACRONYM = """
M. Douglas has arrived.
 M. Douglas has arrived.
Did M. Douglas arrive?
Who just arrived? M.
M.A. Douglas spoke about lang arts.
Sr. Douglas is not here
"""

rACRONYM = """
M_ Douglas has arrived.
 M_ Douglas has arrived.
Did M_ Douglas arrive?
Who just arrived? M.
M_A_ Douglas spoke about lang arts.
Sr_ Douglas is not here
"""

CONTRACTIONS = """
I won't expand them or you can't?
I haven't the right skills for that.
I'll train more, i'm in the right path.
I'd switch to plural, so we're glad,
but isn't easy.
I've done it!
"""

eCONTRACTIONS = """
I will not expand them or you can not?
I have not the right skills for that.
I will train more, i am in the right path.
I would switch to plural, so we are glad,
but is not easy.
I have done it!
"""

(r'won\'t', 'will not'),
(r'can\'t', 'can not'),
(r'i\'m', 'i am'),
(r'isn\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'d(?=\w+ed)', '\g<1> had'), #TODO add rules for irregular verbs
#(r'(\w+)\'s', '\g<1> is'), TODO: Remember to add possessive rules 
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')

rPUNCTUATION = """
For other optional flags of opencv_createsamples see the official . _ 
documentation at http Docs opencv org doc user_guide ug_traincascade 
html . 99 www it ebooks info . Generating Haar Cascades for Custom 8 . 
4 Targets . Creating cascade by running . opencv_traincascade 3_ anoche . 
4 Después . Over 110 recipes to master this full stack Python web 
framework 1 . Take your web2py skills to the next level by dipping 
into delicious"""

eWDOT = """For other (optional) flags of <opencv_createsamples>, see the official... documentation
at http://Docs.opencv.org/doc/user_guide/ug_traincascade.html .
 [ 99 ]
www.it-ebooks.info .
 Generating Haar Cascades for Custom 8.4 Targets
Creating <cascade> by running:
<opencv_traincascade>
3. anoche .
 4 Después. .  .
"""