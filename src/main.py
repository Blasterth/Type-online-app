import socket
from PyQt5.QtGui import QCursor, QFont, QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.sip import delete
import pymysql
from email_validator import validate_email
import random
from pathlib import Path

path = str(Path.cwd())

connection = pymysql.connect() # Database inforamtions ( not in github )
cursor = connection.cursor()

words = ['scarf', 'possible', 'lettuce', 'voice', 'rainstorm', 'loving', 'extra-small', 'flagrant', 'ambiguous', 'trains', 'yard', 'godly', 'lighten', 'nutritious', 'rod', 'toys', 'greedy', 'belief', 'behavior', 'alike', 'lively', 'kneel', 'oafish', 'squirrel', 'energetic', 'dinner', 'crime', 'chalk', 'dam', 'bomb', 'mourn', 'detect', 'onerous', 'rabid', 'chase', 'tap', 'unsuitable', 'texture', 'change', 'mute', 'bit', 'payment', 'sink', 'cows', 'hushed', 'fat', 'flock', 'cent', 'roasted', 'obtain', 'prepare', 'letter', 'bushes', 'fax', 'heat', 'subdued', 'cold', 'nod', 'snobbish', 'pin', 'wrathful', 'flood', 'comb', 'airplane', 'visitor', 'frightening', 'maid', 'knife', 'hideous', 'previous', 'glue', 'pancake', 'round', 'tempt', 'peel', 'habitual', 'moldy', 'fold', 'icy', 'digestion', 'minister', 'reject', 'race', 'flap', 'yam', 'gullible', 'obsequious', 
'welcome', 'grape', 'grey', 'border', 'bone', 'identify', 'dysfunctional', 'destruction', 'repair', 'system', 'tidy', 'terrible', 'branch', 'imperfect', 'like', 'add', 'pale', 'glistening', 'charge', 'splendid', 'swim', 'unwritten', 'juicy', 'reflect', 'public', 'hobbies', 'tumble', 'abortive', 'cloistered', 'thought', 'whine', 'bashful', 'actor', 'scattered', 'flashy', 'slippery', 'pear', 'accessible', 'rat', 'fuzzy', 'pop', 
'early', 'fireman', 'calendar', 'leather', 'overt', 'shiny', 'lip', 'bath', 'substantial', 'education', 'hose', 'recognise', 'tub', 'women', 'holiday', 'jellyfish', 'nauseating', 'shy', 'jeans', 'fumbling', 'shivering', 'play', 'post', 'awake', 'reproduce', 'work', 'grandfather', 'smash', 'attack', 'mailbox', 'tense', 'cap', 'awful', 'rake', 'sudden', 'verse', 'spray', 'puzzling', 'apparatus', 'wind', 'happy', 'null', 'pray', 
'legal', 'degree', 'truck', 'labored', 'stranger', 'sticks', 'curved', 'tremendous', 'nimble', 'erratic', 'statement', 'brick', 'blink', 'earsplitting', 'protect', 'bounce', 'happen', 'plough', 'decisive', 'page', 'fence', 'mint', 'waste', 'weight', 'complain', 'stale', 'imagine', 'stormy', 'horn', 'cow', 'aboriginal', 'gate', 'tent', 'children', 'chop', 'vegetable', 'boorish', 'important', 'greet', 'evanescent', 'locket', 'crowded', 'knowledgeable', 'truculent', 'loud', 'haunt', 'religion', 'show', 'suck', 'tranquil', 'lethal', 'trot', 'mass', 'delight', 'tricky', 'cracker', 'separate', 'glossy', 'doubt', 'belong', 'zebra', 'relation', 
'window', 'vagabond', 'marry', 'blood', 'obnoxious', 'basket', 'ring', 'flippant', 'kick', 'bore', 'painful', 'threatening', 'sound', 'stupendous', 'ordinary', 'pick', 'challenge', 'brawny', 'birth', 'horse', 'physical', 'coat', 'underwear', 'queen', 'utter', 'peep', 'planes', 'calm', 'agonizing', 'dislike', 'high-pitched', 'art', 'turkey', 'grouchy', 'direction', 'kitty', 'wasteful', 'iron', 'receive', 'baseball', 'fruit', 'wren', 'striped', 'creator', 'well-groomed', 'lace', 'woebegone', 'friends', 'abundant', 'savory', 'wealthy', 'tooth', 'prevent', 'rule', 'wish', 'veil', 'book', 'toad', 'unwieldy', 'comparison', 'jog', 'breezy', 'tow', 'company', 'tired', 'rose', 'melt', 'longing', 'eight', 'ink', 'astonishing', 'telling', 'stimulating', 'bizarre', 'pleasant', 'aquatic', 'clear', 'yawn', 'injure', 'utopian', 'observation', 'concern', 'force', 
'zesty', 'discussion', 'reading', 'moor', 'wealth', 'value', 'drum', 'mundane', 'symptomatic', 'confess', 'cat', 'excellent', 'robin', 'permissible', 'dark', 'approve', 'capricious', 'unnatural', 'star', 'thunder', 
'fanatical', 'unaccountable', 'person', 'nippy', 'freezing', 'common', 'heavy', 'grade', 'preach', 'balance', 'rub', 'scorch', 'needle', 'worried', 'scary', 'daily', 'worry', 'circle', 'wood', 'skip', 'powder', 'substance', 'pointless', 'arrange', 'lyrical', 'replace', 'guide', 'obtainable', 'rambunctious', 'sky', 'last', 'cooing', 'rings', 'cautious', 'snotty', 'playground', 'abject', 'error', 'approval', 'harass', 'activity', 'abrasive', 'vest', 'wise', 'cannon', 'few', 'magnificent', 'wiry', 'water', 'disapprove', 'vivacious', 'potato', 'typical', 'well-to-do', 'channel', 'kill', 'whistle', 'beneficial', 'uppity', 'duck', 'worm', 'treat', 'noxious', 'hover', 'distance', 'furniture', 'explain', 'abashed', 'laughable', 'cynical', 'oil', 'coordinated', 'notebook', 'gray', 'pizzas', 'breakable', 'seed', 'classy', 'stain', 'royal', 'impulse', 'downtown', 'scarce', 'possessive', 'pie', 'paltry', 'blow', 'needless', 'acceptable', 'cause', 'barbarous', 'wholesale', 'lunchroom', 'gold', 'courageous', 'exciting', 'dead', 'spicy', 'town', 'suppose', 'war', 'attend', 
'guitar', 'earthy', 'soothe', 'night', 'combative', 'sister', 'measure', 'vase', 'macho', 'cats', 'cycle', 'fetch', 'telephone', 'yellow', 'roll', 'productive', 'chilly', 'mug', 'dance', 'quixotic', 'helpful', 'momentous', 'ghost', 'maniacal', 'tight', 'draconian', 'tough', 'bury', 'wiggly', 'cherry', 'cool', 'rain', 'end', 'sloppy', 'filthy', 'half', 'innocent', 'odd', 'bang', 'tire', 'messy', 'cheer', 'educated', 'spooky', 'equable', 'weary', 'want', 'quicksand', 'expect', 'jewel', 'hang', 'occur', 'bottle', 'bedroom', 'can', 'sand', 'efficacious', 'size', 'trap', 'ossified', 'deadpan', 'nervous', 'quartz', 'doll', 'careless', 'bridge', 'ugly', 'handy', 'adventurous', 'saw', 'useless', 'please', 'friend', 'bell', 'amused', 'high', 'wait', 'trade', 'craven', 'aromatic', 'imported', 'vengeful', 'huge', 'sneaky', 'spare', 'aggressive', 'notice', 'design', 'flawless', 'gather', 'cry', 'fade', 'relax', 'burst', 'punish', 'first', 'compete', 'many', 'stocking', 'wry', 'capable', 'holistic', 'optimal', 'sense', 'canvas', 'dry', 'school', 'nation', 'vigorous', 'frightened', 'tasteless', 'slap', 'kiss', 'idea', 'thaw', 'pets', 'nostalgic', 'real', 'knotty', 'beginner', 'awesome', 'needy', 'fit', 'comfortable', 'dream', 'silent', 'loutish', 'ladybug', 'servant', 'measly', 'closed', 'confused', 'spot', 'deserted', 'uneven', 'allow', 'immense', 'rabbits', 'defective', 'wacky', 'swanky', 'fallacious', 'aunt', 'mighty', 'amount', 'check', 'pine', 'ancient', 'square', 'annoyed', 'borrow', 'wilderness', 'shocking', 'rare', 'spill', 'quiet', 'great', 'scintillating', 'gratis', 'act', 'uttermost', 'memorize', 'cute', 'correct', 'absent', 'zonked', 'offer', 'waggish', 'jam', 'argument', 'invite', 'ruddy', 'brief', 'addition', 'level', 'obscene', 'itch', 'respect', 'unite', 'side', 'kettle', 'treatment', 'wobble', 'strengthen', 'cruel', 'callous', 'satisfying', 'disagree', 'ambitious', 'lumpy', 'unadvised', 'grotesque', 'lame', 'introduce', 'consider', 'division', 'rude', 'mellow', 'arrest', 'poised', 'protest', 'thoughtless', 'ugliest', 'impolite', 'eggs', 'bucket', 'womanly', 'passenger', 'shoe', 'flight', 'dust', 'marvelous', 'fluttering', 'pink', 'transport', 'men', 'cuddly', 'slim', 'illegal', 'steep', 'remember', 'pushy', 'modern', 'pedal', 'glib', 'twist', 'interesting', 'attach', 'abrupt', 'arrive', 'group', 'bouncy', 'little', 'judge', 'reward', 'five', 'possess', 'groovy', 'dirt', 'connect', 'bumpy', 'plucky', 'rustic', 'grip', 'object', 'old-fashioned', 'unused', 'undress', 'good', 'bite-sized', 'health', 'exuberant', 'even', 'unable', 'pocket', 'knee', 'advise', 'suspect', 'interest', 'stream', 'tremble', 'plug', 'rejoice', 'calculator', 'silky', 'afterthought', 'feeble', 'voracious', 'nutty', 'lie', 'woozy', 'representative', 'taste', 'houses', 'temporary', 'crabby', 'wrong', 'partner', 'bare', 'wandering', 'oven', 'snail', 'extra-large', 'elderly', 'witty', 'toy', 'soft', 'spectacular', 'statuesque', 'gamy', 'crowd', 'continue', 'diligent', 'decision', 'boring', 'scratch', 'loose', 'lucky', 'analyze', 'chicken', 'cushion', 'riddle', 'caption', 'road', 'makeshift', 'soggy', 'calculating', 'decide', 'plants', 'house', 'butter', 'double', 'thin', 'badge', 'soda', 'examine', 'low', 'selection', 'sweater', 'sleet', 'violet', 'fish', 'skillful', 'wail', 'nine', 'rainy', 'busy', 'precious', 'invincible', 'detail', 'sign', 'boiling', 'knot', 'next', 'color', 'vague', 'delay', 'clean', 'harbor', 'oranges', 'crayon', 'tender', 'disagreeable', 'file', 'muddled', 'feigned', 'warm', 'afraid', 'rot', 'mate', 'nebulous', 'daughter', 'icicle', 'rigid', 'trees', 'piquant', 'card', 'impress', 'hallowed', 'machine', 'ruthless', 'imaginary', 'egg', 'apparel', 'advice', 'equal', 'example', 'agreeable', 'run', 'hug', 'switch', 'encourage', 'true', 'tenuous', 'shade', 'faithful', 'electric', 'near', 'humdrum', 'powerful', 'grandiose', 'touch', 'intelligent', 'eatable', 'quickest', 'dispensable', 'well-made', 'absorbing', 'embarrassed', 'copper', 'irritating', 'turn', 'railway', 'agree', 'wine', 'cattle', 'suffer', 'blade', 'carve', 'flower', 'library', 'quince', 'watch', 'berry', 'rebel', 'corn', 'disgusted', 'towering', 'vulgar', 'wave', 'babies', 'knowing', 'uninterested', 'wriggle', 'thoughtful', 'drab', 'improve', 'back', 'pail', 'story', 'lamentable', 'swift', 'teaching', 'sleep', 'hulking', 'calculate', 'stew', 'pan', 'church', 'inject', 'line', 'button', 'boot', 'taboo', 'unfasten', 'curtain', 'bubble', 'view', 'terrific', 'minor', 'charming', 'umbrella', 'cloth', 'terrify', 'simple', 'condemned', 'premium', 'voiceless', 'unkempt', 'spiders', 'dizzy', 'stupid', 'reason', 'cheerful', 'slope', 'record', 'plate', 'orange', 'old', 'panicky', 'unknown', 'anger', 'mark', 'perform', 'festive', 'girl', 'chemical', 'space', 'pleasure', 'absurd', 'silly', 'invention', 'frantic', 'zoom', 'frequent', 'entertain', 'press', 'strip', 'chew', 'stroke', 'cooperative', 'belligerent', 'hand', 'remarkable', 'fry', 'crook', 'heavenly', 'chickens', 'position', 'zealous', 'assorted', 'answer', 'wink', 'admit', 'blind', 'sisters', 'burly', 'plantation', 'bat', 'flowers', 'hospital', 'event', 'mother', 'day', 'jelly', 'label', 'ritzy', 'sturdy', 'plastic', 'chance', 'guard', 'applaud', 'wipe', 'chess', 'short', 'seal', 'camera', 'insurance', 'license', 'rob', 'pies', 'black-and-white', 'songs', 'move', 'dirty', 'desire', 'second-hand', 'decorous', 'dinosaurs', 'observe', 'lunch', 'gainful', 'eminent', 'mountain', 'worthless', 'crazy', 'hole', 'stretch', 'large', 'opposite', 'far-flung', 'conscious', 'mist', 'ship', 'talented', 'omniscient', 'glamorous', 'stingy', 'crash', 'placid', 'tomatoes']

from mainpage import Ui_MainWindow
from login import Ui_LonginWindow
from signup import Ui_SignupWindow
from acountSettings import Ui_AcountSettings
from competitions import Ui_CompetitionWindow

class CompetitionWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_CompetitionWindow()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = CompetitionWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class AcountSettingsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_AcountSettings()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = AcountSettingsWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class SignupWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = SignupWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_LonginWindow()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = LoginWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.main = Ui_MainWindow()
        self.main.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #===========================My codes===================
        
        # windows
        self.login = LoginWindow()
        self.signup = SignupWindow()
        self.acountsettings = AcountSettingsWindow()

        # get ips from database | check if its new or not
        cursor.execute("SELECT ip FROM acounts;")
        self.ips = []
        for ip in cursor:
            self.ips.append(ip[0])

        self.userip = str(socket.gethostname())
        if self.userip in self.ips:
            cursor.execute("SELECT username FROM acounts WHERE ip=\'%s\' ;" % self.userip)
            for row in cursor:
                self.username = row[0]
            
            self.openMainWindow(self.username)
        else:
            self.logingin()

        # check typed word
        self.correct_words = 0
        self.wrong_words = 0
        self.correct_letters = 0
        self.wrong_letter = 0

        # competitions
        self.main.btn_createcompetition.clicked.connect(lambda: self.competitionsPage(new=True))
        self.main.btn_joincompetition.clicked.connect(lambda: self.competitionsPage(new=False))

    #===============================Designer codes=============
    def borders(self):
        self.mainwindow = RootMain()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    #===============================My funcitons================
    
    # open signin or login page
    def logingin(self):
        connection.ping(reconnect=True)

        def LoginToDB():
            correct_info = True

            # check blanks
            if ((self.login.ui.username_en.text()).strip() == '') or ((self.login.ui.password_en.text()).strip() == ''):
                self.login.ui.alarmlb.setText('Fill all blanks')
            else:
                # check username
                cursor.execute("SELECT username FROM acounts;")
                db_usernames = []
                for username in cursor:
                     db_usernames.append(username[0])
                if self.login.ui.username_en.text() not in db_usernames:
                    self.login.ui.alarmlb.setText('Username does not exists')
                    correct_info = False

                else:
                    # check password
                    cursor.execute("SELECT password FROM acounts WHERE username=\'%s\' ;" % self.login.ui.username_en.text())
                    password = ''
                    for row in cursor:
                        password = row[0]

                    if self.login.ui.password_en.text() != password:
                        self.login.ui.alarmlb.setText('Username or Password is not correct')
                        correct_info = False

            # change user ip in database
            if correct_info == True:
                quary = "UPDATE acounts SET ip=\'%s\' WHERE username=\'%s\' ;" % (str(socket.gethostname()) , self.login.ui.username_en.text())
                cursor.execute(quary)
                connection.commit()

                self.openMainWindow(self.login.ui.username_en.text())

        # sign in page
        def signing():
            self.login.close()
            self.signup.show()

            def putInfoToDB():

                # check infos
                correct_info = True

                # check blanks
                if ((self.signup.ui.username_en.text()).strip() == '') or ((self.signup.ui.email_en.text()).strip() == '') or ((self.signup.ui.password_en.text()).strip() == '') or ((self.signup.ui.repassword_en.text()).strip() == ''):
                    self.signup.ui.alarmlb.setText('Fill all the blanks') 
                    correct_info = False
                else:
                    # check password
                    numbers = '1234567890'
                    alphabets = 'mnbvcxzasdfghjklpoiuytrewqMNBVCXZASDFGHJKLPOIUYTREWQ'
                    signs = '!@#$%^&*()_-/+'
                    if self.signup.ui.password_en.text() != self.signup.ui.repassword_en.text():
                        self.signup.ui.alarmlb.setText('Passwords are not the same')
                        correct_info = False

                    else:
                        check_pass = [False , False , False]
                        for letter in self.signup.ui.password_en.text():
                            if (letter not in numbers) and (letter not in alphabets) and (letter not in signs):
                                self.signup.ui.alarmlb.setText('Password should contains numbers and alphabets and signs')
                                correct_info = False
                            else:
                                if letter in numbers:
                                    check_pass[0] = True
                                elif letter in alphabets:
                                    check_pass[1] = True
                                elif letter in signs:
                                    check_pass[2] = True
                        
                        if check_pass != [True , True , True]:
                            self.signup.ui.alarmlb.setText('Password should contains numbers and alphabets and signs')
                            correct_info = False
                        else:
                            self.signup.ui.alarmlb.setText('')

                    # check email     
                    try:
                        validate_email(self.signup.ui.email_en.text())

                        cursor.execute("SELECT email FROM acounts;")
                        db_emails = []
                        for email in cursor:
                            db_emails.append(email[0])
                        if self.signup.ui.email_en.text() in db_emails:
                            self.signup.ui.alarmlb.setText('Email already exists')
                            correct_info = False

                    except:
                        self.signup.ui.alarmlb.setText('Email address is not valid')
                        correct_info = False

                    # check username
                    for letter in self.signup.ui.username_en.text():
                        if (letter not in numbers) and (letter not in alphabets) and (letter not in signs):
                            self.signup.ui.alarmlb.setText('Username is not valid')
                            correct_info = False
                        else:
                            cursor.execute("SELECT username FROM acounts;")
                            db_usernames = []
                            for username in cursor:
                                db_usernames.append(username[0])
                            if self.signup.ui.username_en.text() in db_usernames:
                                self.signup.ui.alarmlb.setText('Username already exists')
                                correct_info = False
                            break
                
                # insert infos to database
                if correct_info == True:
                    try:
                        username = self.signup.ui.username_en.text()
                        email = self.signup.ui.email_en.text()
                        password = self.signup.ui.password_en.text()
                        ip = str(socket.gethostname())
                        quary = "INSERT INTO acounts VALUES( \'%s\' , \'%s\' , \'%s\' , \'%s\' , \'%i\' , \'%i\' , \'%i\' , \'%i\' );" % (username , email , password , ip , 0 , 0 , 0 , 0)
                        cursor.execute(quary)
                        connection.commit()

                        self.openMainWindow(username)
                    except:
                        error_msg = QMessageBox()
                        error_msg.setIcon(QMessageBox.Information)
                        error_msg.setText("Someting went wrong")
                        error_msg.setWindowTitle("Error")
                        error_msg.setStandardButtons(QMessageBox.Ok )
                        error_msg.buttonClicked.connect(lambda: error_msg.close())
                        error_msg.exec_()
                    
            


            self.signup.ui.btn_login.clicked.connect(self.logingin)
            self.signup.ui.btn_signup.clicked.connect(putInfoToDB)


        # login page
        self.login.show()
        self.signup.close()
        self.login.ui.btn_signup.clicked.connect(signing)
        self.login.ui.btn_login.clicked.connect(LoginToDB)


    def openMainWindow(self , username):
        connection.ping(reconnect=True)
        self.show()
        self.login.close()
        self.signup.close()

        # acount page
        self.acountPage(username)

        # open & close sidebar
        def openSidebar():
            geo = self.main.sidebar.geometry()
            if geo == QRect(-180, 0, 180, 620):
                self.anim = QPropertyAnimation(self.main.sidebar , b"geometry")
                self.anim.setDuration(200)
                self.anim.setStartValue(QRect(-180, 0, 180, 620))
                self.anim.setEndValue(QRect(0, 0, 180, 620))
                self.anim.start()
                icon3 = QIcon()
                icon3.addPixmap(QPixmap("%s/img/close-menu.png" % path), QIcon.Normal, QIcon.Off)
                self.main.btn_menu.setIcon(icon3)
                self.main.btn_menu.setIconSize(QSize(30, 30))
            else:
                self.anim = QPropertyAnimation(self.main.sidebar , b"geometry")
                self.anim.setDuration(200)
                self.anim.setStartValue(QRect(0, 0, 180, 620))
                self.anim.setEndValue(QRect(-180, 0, 180, 620))
                self.anim.start()
                icon3 = QIcon()
                icon3.addPixmap(QPixmap("%s/img/menu.png" % path), QIcon.Normal, QIcon.Off)
                self.main.btn_menu.setIcon(icon3)
                self.main.btn_menu.setIconSize(QSize(20, 20))

        # move between pages
        self.main.btn_pageTest.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_type),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            connection.ping(reconnect=True)
        ])
        self.main.btn_pageAcount.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_acount),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            connection.ping(reconnect=True)
        ])
        self.main.btn_pageRanking.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_ranking),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.rankingPage(0),
            connection.ping(reconnect=True)
        ])
        self.main.btn_pageCompetitions.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_competitions),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            connection.ping(reconnect=True)
        ])
        self.main.btn_pageSettings.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_settings),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            connection.ping(reconnect=True)
        ])
        # open & close sidebar
        self.main.btn_menu.clicked.connect(openSidebar)

        # test function
        def TypingTest():
            # set words to type
            words_toType = ''
            for this in range(350):
                words_toType += str(words[random.randint(0 , len(words)-1)]) + ' '
            words_toType_list = words_toType.split()
            self.main.type_words.setText(words_toType)
            self.main.type_lastword.setText(words_toType_list[0])

            # delete last results
            self.main.type_cwords.setText('')
            self.main.type_wWords.setText('')
            self.main.type_cletters.setText('')
            self.main.type_Wletters.setText('')
            self.main.type_result.setText('')

            # split words with space
            def splitSpace():
                typed_text = self.main.words_en.text()
                if len(typed_text) == 0:
                    typed_text = 'j'

                if typed_text[-1] == ' ':
                    # check word                    
                    self.checkWord(words_toType_list[0] , typed_text.strip())

                    # delete last word
                    words_toType_list.pop(0)
                    words_toType = ''
                    for word in words_toType_list:
                        words_toType += word + ' '
                    self.main.type_words.setText(words_toType)
                    self.main.type_lastword.setText(words_toType_list[0])
                    self.main.words_en.setText('')
                    

            self.main.words_en.textChanged.connect(splitSpace)
            self.main.words_en.setEnabled(True)
            self.main.words_en.setFocus()

            # test timer
            def typing_timer():
                self.main.type_timer.setText(str(self.main.timer_counter))

                if self.main.timer_counter == 0:
                    self.main.timer.stop()

                    # check if last space has not pushed
                    if self.main.words_en.text() != '':
                        self.checkWord(words_toType_list[0] , self.main.words_en.text().strip())

                    self.main.words_en.setText('')
                    self.main.words_en.setEnabled(False)

                    # print the results
                    self.main.type_cwords.setText("%s Words" % self.correct_words)
                    self.main.type_wWords.setText("%s Words" % self.wrong_words)
                    self.main.type_cletters.setText("%s Letters" % self.correct_letters)
                    self.main.type_Wletters.setText("%s Letters" % self.wrong_letter)
                    
                    self.result = int((self.correct_letters / 5) / 1) # result formula = (characters / 5) / 1 min
                    self.main.type_result.setText("%s WPM" % self.result)

                    # acount
                    self.acount_info['testsTaken'] += 1
                    best = self.acount_info['bestTest']
                    if self.result > best:
                        self.acount_info['bestTest'] = self.result
                    self.acount_info['typedLetters'] += self.correct_letters
                    self.acountPage(username)

                    self.rankingPage(self.result)

                self.main.timer_counter -= 1

            # test timer
            self.main.timer_counter = 60
            self.main.timer = QTimer()
            self.main.timer.timeout.connect(typing_timer)
            self.main.timer.start(100)
        
        self.main.words_en.setEnabled(False)
        self.main.type_restart.clicked.connect(TypingTest)
        
        

    # check typed word and add information fo self attributes
    def checkWord(self , the_word , en_word):
        if en_word == the_word:
            self.correct_words += 1
            self.correct_letters += len(the_word)
        else:
            self.wrong_words += 1
            if len(en_word) == len(the_word):
                counter = -1
                for i in the_word:
                    counter += 1
                    if the_word[counter] == en_word[counter]:
                        self.correct_letters += 1
                    else:
                        self.wrong_letter += 1
            else:
                diff = abs(len(en_word) - len(the_word))
                if len(en_word) > len(the_word):
                    counter = -1
                    for i in the_word:
                        counter += 1
                        if the_word[counter] == en_word[counter]:
                            self.correct_letters += 1
                        else:
                            self.wrong_letter += 1
                    self.wrong_letter += diff
                else:
                    counter = -1
                    for i in en_word:
                        counter += 1
                        if the_word[counter] == en_word[counter]:
                            self.correct_letters += 1
                        else:
                            self.wrong_letter += 1


    # acount page
    def acountPage(self , username):
        connection.ping(reconnect=True)

        # change acount settings
        def changeAcountSetting():
            self.acountsettings.show()

            def change():
                new_username = self.acountsettings.ui.username_en.text()
                new_email = self.acountsettings.ui.email_en.text()
                cursor.execute("SELECT username,email FROM acounts;")
                db_usernames = []
                db_emails = []
                for row in cursor:
                    db_usernames.append(row[0])
                    db_emails.append(row[1])
                if new_username in db_usernames:
                    self.acountsettings.ui.alarmlb.setText("Username already exists")
                elif new_email in db_emails:
                    self.acountsettings.ui.alarmlb.setText("Email already exists")
                else:
                    # change username
                    if new_email.strip() != '':
                        try:
                            validate_email(self.acountsettings.ui.email_en.text())

                            quary = "UPDATE acounts SET email=\'%s\' WHERE email=\'%s\' ;" % (new_email , self.main.acount_email.text())
                            cursor.execute(quary)
                            connection.commit()

                            self.main.acount_email.setText(new_email) # change username from acount page

                        except:
                            self.acountsettings.ui.alarmlb.setText('Email address is not valid')
                    
                    # change email
                    if new_username.strip() != '':
                        quary = "UPDATE acounts SET username=\'%s\' WHERE username=\'%s\' ;" % (new_username , self.main.acount_username.text())
                        cursor.execute(quary)
                        connection.commit()

                        self.main.acount_username.setText(new_username) # change email from acount page
                        self.main.acount_profile.setText(new_username[0].upper())
                    
                    self.acountsettings.close()
                    

            # acount settings page buttons
            self.acountsettings.ui.btn_cancel.clicked.connect(lambda: self.acountsettings.close())
            self.acountsettings.ui.btn_save.clicked.connect(change)

        # log out
        def logOut():
            msg_logout = QMessageBox.question(self, 'LogOut', "Do want to log out from acount?", QMessageBox.Yes | QMessageBox.No)
            if msg_logout == QMessageBox.Yes:
                self.close()
                quary = "UPDATE acounts SET ip=\'\' WHERE username=\'%s\' ; " % self.main.acount_username.text()
                cursor.execute(quary)
                connection.commit()
                self.logingin()


        try:
            cursor.execute("UPDATE acounts SET testsTaken=%i , bestTest=%i , typedWords=%i , competeTaken=%i WHERE username=\'%s\' ;" %
            (self.acount_info['testsTaken'] , self.acount_info['bestTest'] , self.acount_info['typedLetters'] , self.acount_info['competeTaken'] , username)
            )
            connection.commit()
        except:
            pass
        
        cursor.execute("SELECT * FROM acounts WHERE username=\'%s\' ;" % username)
        self.acount_info = {}
        for row in cursor:
            self.acount_info['username'] = row[0]
            self.acount_info['email'] = row[1]
            self.acount_info['testsTaken'] = row[4]
            self.acount_info['bestTest'] = row[5]
            self.acount_info['typedLetters'] = row[6]
            self.acount_info['competeTaken'] = row[7]

        self.main.acount_email.setText(self.acount_info['email'])
        self.main.acount_username.setText(self.acount_info['username'])
        self.main.acount_profile.setText(username[0].upper())
        self.main.acount_teststaken.setText("%s Tests" % self.acount_info['testsTaken'])
        self.main.acount_besttest.setText("%s WPM" % self.acount_info['bestTest'])
        self.main.acount_typedwords.setText("%s Letters" % self.acount_info['typedLetters'])
        self.main.acount_comtaken.setText("%s Competitions" % self.acount_info['competeTaken'])

        try:
            self.tests_avrage = int( (int(self.acount_info['typedLetters']) / 5) / (int(self.acount_info['testsTaken']))) # (typedWords / 5) / (testsTaken * 1)
        except:
            self.tests_avrage = 0
        self.main.acount_testavrage.setText("%s WPM" % self.tests_avrage)

        self.main.btn_acountSettings.clicked.connect(changeAcountSetting)
        self.main.btn_logout.clicked.connect(logOut)


    # ranking page
    def rankingPage(self , wpm):
        connection.ping(reconnect=True)

        cursor.execute("SELECT * FROM ranking;")

        # check if it's in 5 bests
        ranking = {} # username : wpm
        for row in cursor:
            if (row[0] in ranking):
                if ranking[row[0]] < row[1]:
                    ranking[row[0]] = row[1]
            else:
                ranking[row[0]] = row[1]

        
        wpms = list(ranking.values())
        users = list(ranking.keys())
        counter = -1
        for this in wpms:
            counter += 1
            if wpm > this:
                ranking[str(self.main.acount_username.text())] = ranking.pop(users[counter])
                ranking[str(self.main.acount_username.text())] = wpm

                quary = "UPDATE ranking SET username=\'%s\',wpm=%i WHERE wpm=%i ;" % (self.main.acount_username.text() , wpm , this)
                cursor.execute(quary)
                connection.commit()

                break

        # print ranks in ranking page
        sorted_ranks = sorted(ranking.items() , key = lambda x: (-x[1] , x[0]))
        try:
            self.main.rank_user1.setText(sorted_ranks[0][0])
            self.main.rank_test1.setText(str(sorted_ranks[0][1]))
        except:
            self.main.rank_user1.setText('-')
            self.main.rank_test1.setText('-')
        try:
            self.main.rank_user2.setText(sorted_ranks[1][0])
            self.main.rank_test2.setText(str(sorted_ranks[1][1]))
        except:
            self.main.rank_user2.setText('-')
            self.main.rank_test2.setText('-')
        try:
            self.main.rank_user3.setText(sorted_ranks[2][0])
            self.main.rank_test3.setText(str(sorted_ranks[2][1]))
        except:
            self.main.rank_user3.setText('-')
            self.main.rank_test3.setText('-')
        try:
            self.main.rank_user4.setText(sorted_ranks[3][0])
            self.main.rank_test4.setText(str(sorted_ranks[3][1]))
        except:
            self.main.rank_user4.setText('-')
            self.main.rank_test4.setText('-')
        try:
            self.main.rank_user5.setText(sorted_ranks[4][0])
            self.main.rank_test5.setText(str(sorted_ranks[4][1]))
        except:
            self.main.rank_user5.setText('-')
            self.main.rank_test5.setText('-')
            


    # competitions
    def competitionsPage(self , new):
        connection.ping(reconnect=True)

        # open competition page
        def competitionPage(room_code):
            self.comPage = CompetitionWindow()
            self.close()
            self.comPage.show()

            quary = "SELECT host FROM %s ; " % room_code
            cursor.execute(quary)
            for row in cursor:
                is_host = row[0]
            
            if is_host != 1:
                self.comPage.ui.btn_endCompetition.deleteLater()
            else:
                self.comPage.ui.btn_endCompetition = QPushButton(self.comPage.ui.centralwidget)
                self.comPage.ui.btn_endCompetition.setGeometry(QRect(20, 570, 150, 30))
                font = QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                self.comPage.ui.btn_endCompetition.setFont(font)
                self.comPage.ui.btn_endCompetition.setCursor(QCursor(Qt.PointingHandCursor))
                self.comPage.ui.btn_endCompetition.setStyleSheet("background-color: #0088CC; color: #FFFFFF;")
                self.comPage.ui.btn_endCompetition.setObjectName("btn_endCompetition")
                self.comPage.ui.btn_endCompetition.setText("End Competition")
                

            self.comPage.ui.competition_code.setText(room_code)

            # end competition
            def endCompetition(room_code):
                connection.ping(reconnect=True)
                msg_end = QMessageBox.question(self.comPage, 'End Competition', "Do want to end the competition?", QMessageBox.Yes | QMessageBox.No)
                if msg_end == QMessageBox.Yes:
                    self.comPage.close()
                    self.show()
                    cursor.execute("DROP TABLE %s ;" % room_code)
                    connection.commit()

            # print competition ranking
            def competitionRanking():
                connection.ping(reconnect=True)
                # delete former ranks
                def deleteRanks():
                    for i in reversed(range(self.comPage.ui.verticalLayout.count())): 
                        self.comPage.ui.verticalLayout.itemAt(i).widget().setParent(None)

                deleteRanks()

                # print new ranks
                tests = {}
                cursor.execute("SELECT * FROM %s" % room_code)
                for row in cursor:
                    tests[row[0]] = row[1]

                ranking = sorted(tests.items() , key = lambda x: -x[1])
                counter = 1
                for rank in ranking:
                    self.comPage.ui.label_4 = QLabel(self.comPage.ui.scrollAreaWidgetContents)
                    sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.comPage.ui.label_4.sizePolicy().hasHeightForWidth())
                    self.comPage.ui.label_4.setSizePolicy(sizePolicy)
                    self.comPage.ui.label_4.setMinimumSize(QSize(0, 40))
                    font = QFont()
                    font.setFamily("Arial")
                    font.setPointSize(9)
                    self.comPage.ui.label_4.setFont(font)
                    self.comPage.ui.label_4.setStyleSheet("background: #DEDEDE;")
                    self.comPage.ui.label_4.setObjectName("label_4")
                    self.comPage.ui.verticalLayout.addWidget(self.comPage.ui.label_4)
                    self.comPage.ui.label_4.setText('   %i.    %s  |   %i WPM' % (counter,rank[0],rank[1]))
                    counter += 1
            

            # competition test
            def competitionTypingTest():
                # set words to type
                words_toType = ''
                for this in range(350):
                    words_toType += str(words[random.randint(0 , len(words)-1)]) + ' '
                words_toType_list = words_toType.split()
                self.comPage.ui.type_words.setText(words_toType)
                self.comPage.ui.type_lastword.setText(words_toType_list[0])

                # delete last results
                self.comPage.ui.type_cwords.setText('')
                self.comPage.ui.type_wWords.setText('')
                self.comPage.ui.type_cletters.setText('')
                self.comPage.ui.type_Wletters.setText('')
                self.comPage.ui.type_result.setText('')

                # split words with space
                def splitSpace():
                    typed_text = self.comPage.ui.words_en.text()
                    if len(typed_text) == 0:
                        typed_text = 'j'

                    if typed_text[-1] == ' ':
                        # check word                    
                        self.checkWord(words_toType_list[0] , typed_text.strip())

                        # delete last word
                        words_toType_list.pop(0)
                        words_toType = ''
                        for word in words_toType_list:
                            words_toType += word + ' '
                        self.comPage.ui.type_words.setText(words_toType)
                        self.comPage.ui.type_lastword.setText(words_toType_list[0])
                        self.comPage.ui.words_en.setText('')
                        

                self.comPage.ui.words_en.textChanged.connect(splitSpace)
                self.comPage.ui.words_en.setEnabled(True)
                self.comPage.ui.words_en.setFocus()

                # test timer
                def typing_timer():
                    self.comPage.ui.type_timer.setText(str(self.comPage.ui.timer_counter))

                    # finish test
                    if self.comPage.ui.timer_counter == 0:
                        self.comPage.ui.timer.stop()

                        # check if last space has not pushed
                        if self.comPage.ui.words_en.text() != '':
                            self.checkWord(words_toType_list[0] , self.comPage.ui.words_en.text().strip())

                        self.comPage.ui.words_en.setText('')
                        self.comPage.ui.words_en.setEnabled(False)

                        # print the results
                        self.comPage.ui.type_cwords.setText("%s Words" % self.correct_words)
                        self.comPage.ui.type_wWords.setText("%s Words" % self.wrong_words)
                        self.comPage.ui.type_cletters.setText("%s Letters" % self.correct_letters)
                        self.comPage.ui.type_Wletters.setText("%s Letters" % self.wrong_letter)
                        
                        self.comPage.result = int((self.correct_letters / 5) / 1) # result formula = (characters / 5) / 1 min
                        self.comPage.ui.type_result.setText("%s WPM" % self.comPage.result)

                        cursor.execute("SELECT bestTest FROM %s WHERE username=\'%s\'" % (room_code , self.main.acount_username.text()))
                        for row in cursor:
                            if self.comPage.result > row[0]:
                                quary = "UPDATE %s SET bestTest=%i WHERE username=\'%s\' ;" % (room_code , self.comPage.result , self.main.acount_username.text())
                                cursor.execute(quary)
                                connection.commit()
                                competitionRanking()


                    self.comPage.ui.timer_counter -= 1

                # test timer
                self.comPage.ui.timer_counter = 60
                self.comPage.ui.timer = QTimer()
                self.comPage.ui.timer.timeout.connect(typing_timer)
                self.comPage.ui.timer.start(100)

            self.comPage.ui.words_en.setEnabled(False)
            self.comPage.ui.type_restart.clicked.connect(competitionTypingTest)

            self.comPage.ui.btn_back.clicked.connect(lambda: [self.comPage.close() , self.show()])
            try:
                self.comPage.ui.btn_endCompetition.clicked.connect(lambda: endCompetition(room_code))
            except:
                pass
            competitionRanking()

        # create new competition
        def createCompetition():
            cursor.execute("show tables;")    
            talbes = []
            for row in cursor:
                talbes.append(row[0])

            # create competition code
            code_characters = '12345678567890qwertyuiopasdfghjklzxcvbnm'
            room_code = ''
            while len(room_code) != 6:
                room_code += random.choice(code_characters)

            if room_code in talbes:
                createCompetition()
            else:
                # create competition talbe in database
                quary = "CREATE TABLE %s (username VARCHAR(100) , bestTest INT , host VARCHAR(100) );" % room_code
                cursor.execute(quary)
                cursor.execute("INSERT INTO %s VALUES (\'%s\' , 0 , 1) ;" % (room_code , self.main.acount_username.text()))
                connection.commit()

                competitionPage(room_code)
            
            
        # join a competition
        def joinCompetition():
            # check blanks
            if self.main.join_competition.text().strip() == '':
                self.main.alarmlb.setText('Please enter competition code')
            else:
                # join to the competition
                cursor.execute('show tables;')
                tables = []
                for row in cursor:
                    tables.append(row[0])
                    
                print('tables:' , tables)
                if self.main.join_competition.text() in tables:
                    self.main.alarmlb.setText('')

                    # insert new user into database
                    cursor.execute("SELECT username FROM %s; " % self.main.join_competition.text())
                    table_users = []
                    for row in cursor:
                        table_users.append(row[0])
                    print('users: ' , table_users)
                    if self.main.acount_username.text() not in table_users:
                        # if user loged for first time
                        quary = "INSERT INTO %s VALUES (\'%s\' , 0 , 0);" % (self.main.join_competition.text() , self.main.acount_username.text())
                        cursor.execute(quary)
                        connection.commit()

                    competitionPage(str(self.main.join_competition.text()))
                else:
                    self.main.alarmlb.setText('This competition does not exists')



        if new == True:
            createCompetition()
        else:
            joinCompetition()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())