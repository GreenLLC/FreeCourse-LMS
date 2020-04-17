FLAKE_ERRORS_MAPPING = {
    'A002': 'יש פה שם משתנה שיש לו משמעות מיוחדת עבור פייתון. בעצם הדריסה של השם הזה אתם לא מאפשרים לגשת אליו יותר. עדיף להמנע מהמצב הזה ולמצוא שם אחר למשתנה שלכם.',
    'B001': 'אסור להשתמש ב־except לבדו. נסו להבין אילו Exceptions עלולים לקפוץ ותפסו אותם בהתאם. אם אין אחד ספציפי כזה, תפסו את Exception.',
    'B005': 'שימוש ב־<code dir="ltr">.strip</code> כשהארגומנט הוא עם מספר תווים גדול מ־1 עלול להראות לקורא כאילו עושים strip לכל המחרוזת (ולא לכל אחד מהתווים בנפרד, וזה קצת מבלבל. אם זה מכוון, ניתן לשים את המחרוזת שמועברת כארגומנט בתוך משתנה קבוע כדי להפוך את הקוד לקריא יותר. אם התכוונתם להוריד תת־מחרוזת ממחרוזת קיימת, השתמשו ב־<code dir="rtl">.replace</code> במקום.',
    'B006': 'חשוב לא להשתמש בסוגי משתנים ברי־שינוי (רשימות, לדוגמה) עבור ברירת־מחדל של פרמטרים. הגדרת ערכי ברירת־המחדל מתבצעת פעם אחת, <strong>בהגדרה</strong> של הפונקציה, ולא כל פעם שהפונקציה נקראת. מהסיבה הזו כל הקריאות לפונקציה ישתמשו במשתנה שהוגדר בהתחלה גם אם הפונקציה שינתה את התוכן שלו, ואותו ערך עלול להשתנות בין קריאות לפונקציה.',
    'B007': 'הגדרת משתנה בלולאה אך לא השתמשת בו בתוך הלולאה.',
    'B008': 'אל תבצעו קריאה לפונקציות ברשימת הפרמטרים. הגדרת הפונקציה נעשית פעם אחת ויחידה, וזה יגרום לערך שעל הפרמטר להשאר קבוע לאורך הריצות שלה.',
    'C407': 'לא חייבים להשתמש כאן ב־list/dict comprehension, הפונקציה יודעת לקבל גנרטור.',
    'C410': 'אין צורך להמיר את הרשימה הזו ל־list. הוציאו אותה מהקריאה לפונקציה.',
    'C416': 'אין צורך להשתמש פה ב־list comprehension, עדיף להשתמש פשוט ב־<code>list()</code>',
    'C819': 'הפסיק פה לא הכרחי.',
    'E111': 'הזחה (הזזה של שורה שמאלה בעזרת רווחים או טאבים) בקוד פייתון נאה חייבת להיות מורכבת מכפולות של 4 רווחים.',
    'E112': 'ציפינו לראות פה הזחה ולא מצאנו אותה :)',
    'E113': 'יש לנו פה בעיה עם ההזחה של הקוד. יש מצב ששורות מסוימות התחילו ברווחים איפה שלא צריך?',
    'E114': 'הזחה (הזזה של שורה שמאלה בעזרת רווחים או טאבים) בקוד פייתון נאה חייבת להיות מורכבת מכפולות של 4 רווחים.',
    'E115': 'קטע ההערה הזה אמור להיות מוזח.',
    'E116': 'משהו לא כל־כך עובד בהזחה פה. בדקו אותה שוב.',
    'E123': 'סגירת הסוגריים צריכה להיות באותה רמת הזחה כמו תחילת השורה שבה הן נפתחו.',
    'E125': 'ההזחה פה אינה מנומסת – עדיף לא לשבור שורה לאותה רמת הזחה כמו השורה הבאה.',
    'E126': 'השורה הזו תלויה באוויר! זה יותר מדי הזחה.',
    'E129': 'בפייתון, זה נחשב לא מנומס להכניס כמה הוראות באותה שורה ולהפריד ביניהן בנקודה־פסיק.',
    'E201': 'כדי לשמור על הקוד מסודר ויפה, מומלץ שלא לשים רווחים אחרי תו של סגירת סוגריים.',
    'E202': 'כדי לשמור על הקוד מסודר ויפה, מומלץ שלא לשים רווחים לפני תו של סגירת סוגריים.',
    'E203': 'מצאנו רווח לפני נקודתיים בשורה הזו. כדי לשמור על הקוד נקי, עדיף להסיר אותן.',
    'E211': 'כדי לשמור על הקוד מסודר ויפה, מומלץ שלא לשים רווחים לפני תו של פתיחת סוגריים.',
    'E221': 'מצאנו יותר מרווח אחד לפני אופרטור בשורה הזו. זה אמנם יעבוד, אבל זה נחשב לא כזה מנומס. תוכלו לתקן בבקשה?',
    'E222': 'מצאנו יותר מרווח אחד אחרי אופרטור בשורה הזו. זה אמנם יעבוד, אבל זה נחשב לא כזה מנומס. תוכלו לתקן בבקשה?',
    'E225': 'חסר לך רווחים מסביב לאופרטור בשורה הזו.',
    'E226': 'חסר לך רווחים מסביב לאופרטור החשבוני בשורה הזו.',
    'E227': 'חסרים רווחים מסביב לאופרטורים הבינאריים בשורה הזו.',
    'E228': 'חסרים לך רווחים מסביב לאופרטור של המודולו.',
    'E231': 'המלצה: נחשב משמעותית יותר יפה לשים רווח אחרי פסיק, ממש כמו בעברית.',
    'E241': 'שמנו לב שיש כמה רווחים אחרי הפסיק פה. זה עובד, אבל זה נראה פחות טוב מבחינת סגנון ונעדיף תמיד רווח בודד אחרי פסיק.',
    'E251': 'נחשב מנומס יותר לא לרווח מסביב לסימן השווה בהעברת ארגומנטים.',
    'E261': 'בשורות קוד בהן מופיעה גם הערה, מקובל לשים לפחות שני רווחים לפני התו סולמית כדי לבדל את הקוד מההערה.',
    'E262': 'הערות צריכות להתחיל בתווים סולמית ואז רווח מיד אחרי.',
    'E265': 'הערות צריכות להתחיל בתווים סולמית ואז רווח מיד אחרי.',
    'E266': 'זה קצת הרבה סולמיות בשביל הערה :) עדיף לא להשאיר שורות כאלו בקוד.',
    'E271': 'מצאנו יותר מרווח אחד אחרי מילת המפתח בשורה הזו. זה אמנם יעבוד, אבל זה נחשב לא כזה מנומס. תוכלו לתקן בבקשה?',
    'E272': 'מצאנו יותר מרווח אחד לפני מילת המפתח בשורה הזו. זה אמנם יעבוד, אבל זה נחשב לא כזה מנומס. תוכלו לתקן בבקשה?',
    'E301': 'כדי לשמור על קוד נקי ויפה, אנחנו ממליצים לעשות פה ריווח של שורה אחת.',
    'E302': 'אנחנו ממליצים פה על 2 ירידות שורה כדי להפריד בין חלקי הקוד.',
    'E303': 'הושארו פה יותר מדי שורות ריקות, צמצמו אותן קצת :)',
    'E305': 'אנחנו ממליצים להפריד בין פונקציות או מחלקות בעזרת 2 ירידות שורה.',
    'E306': 'נהוג לעשות ירידת שורה נוספת לפני הגדרת פונקציות מקוננת.',
    'E402': 'יבוא המודול צריך להופיע בראש הקובץ.',
    'E502': 'אין צורך לשים לוכסן אחורי בין סוגריים.',
    'E701': 'בפייתון, נהוג לא לרשום יותר מביטוי אחד בשורה. סדרו את הקוד כך שכל ביטוי יופיע בשורה נפרדת, והימנעו משימוש בנקודה פסיק.',
    'E702': 'בפייתון, נהוג לא לרשום יותר מביטוי אחד בשורה. סדרו את הקוד כך שכל ביטוי יופיע בשורה נפרדת, והימנעו משימוש בנקודה פסיק.',
    'E703': 'בפייתון אנחנו לא משתמשים בנקודה פסיק כדי לסיים שורות קוד או ביטויים.',
    'E711': 'כאשר משווים לערך None, עדיף להשתמש ב־<code>if variable_name is None</code>.',
    'E712': 'הנה אתגר מעניין: האם אפשר לבדוק שערך שווה ל־True בצורה קצרה יותר?',
    'E713': "כשאנחנו רוצים למצוא האם משהו לא נמצא בתוך משהו אחר, אנחנו נעדיף להשתמש ב־\'not in\'.",
    'E721': 'ניסיון מגניב להשוואת טיפוסים! נסו להשתמש בפונקציה <code>isinstance</code> במקום.',
    'E722': 'אסור להשתמש ב־except לבדו. נסו להבין אילו Exceptions עלולים לקפוץ ותפסו אותם בהתאם. אם אין אחד ספציפי כזה, תפסו את Exception.',
    'E731': 'זו דוגמה למקום שעדיף להגדיר פונקציה מאשר להשתמש ב־lambda.',
    'E741': 'חשוב לנו ששמות המשתנים שלך יהיו טובים. כדאי לבחור שם משתנה בעל משמעות, באותיות קטנות, שמתאר היטב את תוכן המשתנה. אם יש כמה מילים בשם המשתנה, ניתן להשתמש בקו תחתון (_) כדי להפריד אותן אחת מהשנייה.',
    'E902': 'כשהבודק שלנו ניסה להריץ את הקוד שלך, הוא ראה שלפייתון הייתה בעיה בלהבין אותו. יש מצב ששכחת לסגור מקף, גרשיים או סוגריים? זה לא חייב להיות דווקא בשורה הזו, אז כדאי להסתכל קצת למעלה.',
    'E999': 'כשהבודק שלנו ניסה להריץ את הקוד שלך, הוא ראה שלפייתון יש בעיה להבין אותו. כדאי לוודא שהקוד רץ כהלכה לפני שמגישים אותו.',
    'EB007': 'הגדרת משתנה בלולאה אך לא השתמשת בו בתוך הלולאה.',
    'EF841': 'הגדרת משתנה אך לא השתמשת בו.',
    'ES307': 'פונקציה לא מאובטחת. עדיף להשתמש ב־<code>ast.literal_eval</code>',
    'EW191': 'ההזחה פה כוללת טאבים במקום 4 רווחים. אם אתם משתמשים בעורך שאינו jupyter, הקפידו להגדיר אותו כך שימיר לחיצה על טאב לארבעה רווחים.',
    'F401': 'יבאת מודול ולא עשית בו שימוש במהלך הקוד.',
    'F403': 'עדיף שלא לייבא עם כוכבית כשלא ממש חייבים.',
    'F405': 'אחד האובייקטים בשורה הזו לא הוגדר, או שיובא באמצעות כוכבית אחרי ה־import.',
    'F632': 'השתמשו באופרטור == או != כדי להשוות בין מחרוזות ומספרים',
    'F706': 'ביצעת <code>return</code> מחוץ לפונקציה. זה יגרום לקוד לא לרוץ. האם בדקת שהקוד עובד?',
    'F722': 'משהו לא תקין בשורה הזו, סימן הנקודתיים לא אמור להופיע כאן.',
    'F811': 'הגדרת מחדש משתנה או פונקציה שלא נעשה בו שימוש לפני כן.',
    'F821': 'שם המשתנה שמופיע פה לא הוגדר. אם הוא כן הוגדר בתאים אחרים במחברת, הוסיפו אותו לתא כדי שהבודק יוכל להתייחס לפתרון שלכם.',
    'F823': 'בשלב הזה עדיין לא הגדרתם את המשתנה בתוך הפונקציה הזו. הוא כן מוגדר בהמשך, אבל התייחסתם אליו כאן. כבר עכשיו. אם המשתנה הזה שייך לפונקציה הזו הוא חייב להיות מוגדר בתוך הפונקציה לפני שאתם מתייחסים אליו.',
    'F841': 'הגדרת משתנה אך לא השתמשת בו.',
    'I100': 'יבואי המודולים שלך מסודרים לא נכון. הקפידו לסדר אותם בסדר אלפבתי.',
    'I201': 'יבואי המודולים שלך מסודרים לא נכון. יש להקפיד על שורה רווח בין מודולים מונים לבין מודולים שלא באים עם פייתון.',
    'M511': 'חשוב לא להשתמש בסוגי משתנים ברי־שינוי (רשימות, לדוגמה) עבור ברירת־מחדל של פרמטרים. הגדרת ערכי ברירת־המחדל מתבצעת פעם אחת, <strong>בהגדרה</strong> של הפונקציה, ולא כל פעם שהפונקציה נקראת. מהסיבה הזו כל הקריאות לפונקציה ישתמשו במשתנה שהוגדר בהתחלה גם אם הפונקציה שינתה את התוכן שלו, ואותו ערך עלול להשתנות בין קריאות לפונקציה.',
    'N400:': 'לא נהוג להשתמש בלוכסן אחורי כדי לשבור שורות בפייתון. נסו להשתמש בסוגריים במקום :)',
    'S307': 'פונקציה לא מאובטחת. עדיף להשתמש ב־<code>ast.literal_eval</code>.',
    'S610': 'עלול להיות פגיע למתקפות SQL Injection',
    'W191': 'ההזחה פה כוללת טאבים במקום 4 רווחים. אם אתם משתמשים בעורך שאינו jupyter, הקפידו להגדיר אותו כך שימיר לחיצה על טאב לארבעה רווחים.',
    'W291': 'מצאנו שהתגנבו לך רווחים אחרי התו האחרון בשורה. לפתרון מושלם, נקו את הרווחים הללו.',
    'W293': 'השורה הריקה פה מכילה רווחים. לפתרון מושלם, עדיף להוריד אותם.',
    'W503': 'עדיף לשים את האופרטור הלוגי אחרי שבירת השורה.',
}

FLAKE_SKIP_ERRORS = (
    'A001',  # known builtin method override
    'B901',  # return in generatrors
    'B901',  # return in generatrors
    'C812',  # missing trailing comma
    'C812',  # missing trailing comma
    'C813',  # missing trailing comma
    'E117',  # over-indented
    'E122',  # continuation line outdented or dedented
    'E124',  # closing brackets indentation
    'E127',  # continuation line over-indented for visual indent
    'E128',  # continuation line under-indented for visual indent
    'E501',  # > 79
    'E800',  # commented-out code
    'E800:',  # For some reason flake8 sends this key with ':', that's a bug, but not ours
    'Q000',  # bad quotes
    'Q001',  # bad quotes
    'Q002',  # bad quotes on docstring
    'Q003',  # Change outer quotes for internal escaping
    'S101',  # Use of assert detected
    'S311',  # pseudo-random generators warning
    'S322',  # input is a dangerous method of Python 2 yada yada
    'T000',  # todo note found
    'T001',  # print found
    'T002',  # Python 2.x reserved word print used
    'W292',  # no new line in the end of the code
    'W391',  # blank lines at the end of file
    'W504',  # line break after operator
    'W605',  # invalid escape sequence
)
