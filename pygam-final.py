
import pygame
import random,os
from pygame.locals import *
pygame.init()
import pygame.gfxdraw
import pygame.mixer
#320 MINIMUM MOBILE SIZE
import time
di=os.getcwd()+'\\media\\'
pygame.mixer.music.load(di+'music.mp3')
pygame.mixer.music.play(-1)    
class game:       
   
   gameExit = False
   gameStatus = 0 #0- intro 1-wordgame
   gray     = (100, 100, 100)
   navyblue = ( 60,  60, 100)
   white    = (255, 255, 255)

   red     = (255,   0,   0)
   green    = (  0, 255,   0)
   blue     = (  0,   0, 255)
   yellow   = (255, 255,   0)
   orange   = (255, 128,   0)
   purple   = (255,   0, 255)
   cyan     = (  0, 255, 255)

   button1=pygame.image.load(di+'button-on.png')
   button2=pygame.image.load(di+'button-off.png')
   button3=pygame.image.load(di+'button-select.png')
   sprite = pygame.sprite.Sprite()
   disp = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
   #disp = pygame.display.set_mode((800,500))
   dimension= pygame.display.Info()
   wi=dimension.current_w 
   he=dimension.current_h

   print(wi,he)
   size=(wi/40)+(he/40)
   print('size',size)
   font=0
#   w,h=0,0
   def __init__(self):
      print 'Call'


      pygame.init()
      pygame.font.init()

      print "Calling parent constructor"


      self.disp.fill(self.white)
      pygame.display.update()


      #pygame.display.set_mode((w,h))







   def message(self,m,color,x,y,z):
      self.font = pygame.font.SysFont("Times New Roman",z,bold=False,italic=False)
      self.text = self.font.render(m, True, color)
      self.disp.blit(self.text,[x,y])
 
   def rule(self):
      self.disp.fill(self.white)
      pygame.display.update()
      self.font = pygame.font.SysFont("Times New Roman",30,bold=False,italic=False)

      rules =di+"rules.txt"

      inFile = open(rules, 'r', 0)
      w=10
      i=0
      for line in inFile:
         i=i+5
         self.text = self.font.render(line[:-1], True, g.orange)
         self.disp.blit(self.text,[5,w*i])
      pygame.display.update()

      pygame.time.delay(10000)

 

class wordgame(game):
   len1=0
   x1=[]
   list1=[]
   y1=[]
   word_found=[]
   
   wg,hg=0,0
   time_stop=0
   d={}
   tick1=pygame.image.load(di+'tick-on.png')
   cross1=pygame.image.load(di+'cross-on.png')
   tick2=pygame.image.load(di+'tick-off.png')
   cross2=pygame.image.load(di+'cross-off.png')
   textbox=pygame.image.load(di+'box.png')
   textbox2=pygame.image.load(di+'textbox2.png')
   brain=pygame.image.load(di+'brain.png')
   clear=pygame.image.load(di+'large button.png')
   tw,th,cw,ch=0,0,0,0
   lis=[]
   let=[]
   mi,sec=0,0
   sprite = pygame.sprite.Sprite()
   def __init__(self):

      print "Calling parent constructor"
      #pygame.font.init()      

      self.disp.fill(self.white)
      pygame.display.set_caption('Game')
      pygame.display.update()


      #pygame.display.set_mode((w,h))


   def start(self):
      redo=1
      while(redo):
         a=['abandon', 'abandoned', 'ability', 'able','affinity', 'about', 'above', 'abroad', 'absence', 'absent', 'absolute', 'absolutely', 'absorb', 'abuse', 'abuse', 'academic', 'accent', 'accept', 'acceptable', 'access', 'accident', 'accidental', 'accidentally', 'accommodation', 'accompany', 'account', 'accurate', 'accurately', 'accuse', 'achieve', 'achievement', 'acid', 'acknowledge', 'acquire', 'across', 'act', 'action', 'active', 'actively', 'activity', 'actress', 'actual', 'actually', 'ad', 'adapt', 'add', 'addition', 'additional', 'address', 'adequate', 'adequately', 'adjust', 'admiration', 'admire', 'admit', 'adopt', 'adult', 'advance', 'advanced', 'advantage', 'adventure', 'advert', 'advertise', 'advertisement', 'advertising', 'advice', 'advise', 'affair', 'affect', 'affection', 'afford', 'afraid', 'after', 'afternoon', 'afterwards', 'again', 'against', 'age', 'aged', 'agency', 'agent', 'aggressive', 'ago', 'agree', 'agreement', 'ahead', 'aid', 'aim', 'air', 'aircraft', 'airport', 'alarm', 'alarmed', 'alarming', 'alive', 'all', 'allied', 'allow', 'ally', 'almost', 'alone', 'along', 'alongside', 'aloud', 'alphabet', 'alphabetical', 'alphabetically', 'already', 'also', 'alter', 'alternative', 'alternatively', 'although', 'altogether', 'always', 'amaze', 'amazed', 'amazing', 'ambition', 'ambulance', 'among', 'amount', 'amuse', 'amused', 'amusing', 'analyse', 'analysis', 'ancient', 'and', 'anger', 'angle', 'angrily', 'angry', 'animal', 'ankle', 'anniversary', 'announce', 'annoy', 'annoyed', 'annoying', 'annual', 'annually', 'another', 'answer','anticipate', 'anxiety', 'anxious', 'anxiously', 'any', 'anybody', 'anyone', 'anything', 'anyway', 'anywhere', 'apart', 'apartment', 'apologize', 'apparent', 'apparently', 'appeal', 'appear', 'appearance', 'apple', 'application', 'apply', 'appoint', 'appointment', 'appreciate', 'approach', 'appropriate', 'approval', 'approve', 'approving', 'approximate', 'approximately', 'april', 'area', 'argue', 'argument', 'arise', 'arm', 'armed', 'arms', 'army', 'around', 'arrange', 'arrangement', 'arrest', 'arrival', 'arrive', 'arrow', 'art', 'article', 'artificial', 'artificially', 'artist', 'artistic', 'artistically', 'as', 'ashamed', 'aside', 'ask', 'asleep', 'aspect', 'assist', 'assistance', 'assistant', 'associate', 'associated', 'association', 'assume', 'assure', 'at', 'atmosphere', 'attach', 'attached', 'attack', 'attempt', 'attempted', 'attend', 'attention', 'attitude', 'attorney', 'attract', 'attraction', 'attractive', 'audience', 'august', 'aunt', 'author', 'authority', 'automatic', 'automatically', 'autumn', 'available', 'average', 'avoid', 'awake', 'award', 'aware', 'away', 'awful', 'awfully', 'awkward', 'awkwardly']
         b=['baby', 'back', 'background', 'backward', 'backwards', 'bacteria', 'bad', 'badly', 'bag', 'baggage', 'bake', 'balance', 'ball', 'ban', 'band', 'bandage', 'bar', 'bargain', 'barrier', 'base', 'based', 'basic', 'basically', 'basis', 'bath', 'bathroom', 'battery', 'battle', 'bay', 'be', 'beach', 'beak', 'bear', 'beard', 'beat', 'beautiful', 'beautifully', 'beauty', 'because', 'become', 'bed', 'bedroom', 'beef', 'before', 'begin', 'beginning', 'behalf', 'behave', 'behaviour', 'behind', 'belief', 'believe', 'bell', 'belong', 'below', 'belt', 'bend', 'beneath', 'benefit', 'bent', 'beside', 'best', 'bet', 'better', 'betting', 'between', 'beyond', 'bicycle', 'big', 'bike', 'bill', 'billion', 'bin', 'biology', 'bird', 'birth', 'birthday', 'biscuit', 'bit', 'bite', 'bitter', 'bitterly', 'black', 'blade', 'blame', 'blank', 'blind', 'block', 'blonde', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'boil', 'bomb', 'bone', 'book', 'boot', 'border', 'bore', 'bored', 'boring', 'born', 'borrow', 'boss', 'both', 'bother', 'bottle', 'bottom', 'bound', 'bowl', 'box', 'boy', 'boyfriend', 'brain', 'branch', 'brand', 'brave', 'bread', 'break', 'breakfast', 'breast', 'breath', 'breathe', 'breathing', 'breed', 'brick', 'bridge', 'brief', 'briefly', 'bright', 'brightly', 'brilliant', 'bring', 'broad', 'broadcast', 'broadly', 'broken', 'brother', 'brown', 'brush', 'bubble', 'budget', 'build', 'building', 'bullet', 'bunch', 'burn', 'burnt', 'burst', 'bury', 'bus', 'bush', 'business', 'businessman', 'busy', 'but', 'butter', 'button', 'buy', 'buyer', 'by', 'bye']
         c=['cabinet', 'cable', 'cake', 'calculate', 'calculation', 'called', 'calm', 'calmly', 'camera', 'camp', 'campaign', 'camping', 'cancel', 'cancer', 'candidate', 'candy', 'cannot', 'cap', 'capable', 'capacity', 'capital', 'captain', 'capture', 'car', 'card', 'cardboard', 'care', 'career', 'careful', 'carefully', 'careless', 'carelessly', 'carpet', 'carrot', 'carry', 'case', 'cash', 'cast', 'castle', 'cat', 'catch', 'category', 'cause', 'cd', 'cease', 'ceiling', 'celebrate', 'celebration', 'cell', 'cent', 'centimetre', 'central', 'centre', 'century', 'ceremony', 'certain', 'certainly', 'certificate', 'chain', 'chair', 'chairman', 'chairwoman', 'challenge', 'chamber', 'chance', 'change', 'channel', 'chapter', 'character', 'characteristic', 'charge', 'charity', 'chart', 'chase', 'chat', 'cheap', 'cheaply', 'cheat', 'check', 'cheek', 'cheerful', 'cheerfully', 'cheese', 'chemical', 'chemist', 'chemistry', 'cheque', 'chest', 'chew', 'chicken', 'chief', 'child', 'chin', 'chip', 'chocolate', 'choice', 'choose', 'chop', 'church', 'cigarette', 'cinema', 'circle', 'circumstance', 'citizen', 'city', 'civil', 'claim', 'clap', 'class', 'classic', 'classroom', 'clean', 'clear', 'clearly', 'clerk', 'clever', 'click', 'client', 'climate', 'climb', 'climbing', 'clock', 'closed', 'closely', 'closet', 'cloth', 'clothes', 'clothing', 'cloud', 'club', 'coach', 'coal', 'coast', 'coat', 'code', 'coffee', 'coin', 'cold', 'coldly', 'collapse', 'colleague', 'collect', 'collection', 'college', 'colour', 'coloured', 'column', 'combination', 'combine', 'come', 'comedy', 'comfort', 'comfortable', 'comfortably', 'command', 'comment', 'commercial', 'commission', 'commit', 'commitment', 'committee', 'common', 'commonly', 'communicate', 'communication', 'community', 'company', 'compare', 'comparison', 'compete', 'competition', 'competitive', 'complain', 'complaint', 'complete', 'completely', 'complex', 'complicate', 'complicated', 'computer', 'concentrate', 'concentration', 'concept', 'concern', 'concerned', 'concerning', 'concert', 'conclude', 'conclusion', 'concrete', 'conduct', 'conduct', 'conference', 'confidence', 'confident', 'confidently', 'confine', 'confined', 'confirm', 'conflict', 'confront', 'confuse', 'confused', 'confusing', 'confusion', 'congratulate', 'congratulation', 'congress', 'connect', 'connected', 'connection', 'conscious', 'consequence', 'conservative', 'consider', 'considerable', 'considerably', 'consideration', 'consist', 'constant', 'constantly', 'construct', 'construction', 'consult', 'consumer', 'contact', 'contain', 'container', 'contemporary', 'contest', 'context', 'continent', 'continue', 'continuous', 'continuously', 'contract', 'contract', 'contrast', 'contrast', 'contrasting', 'contribute', 'contribution', 'control', 'controlled', 'convenient', 'convention', 'conventional', 'conversation', 'convert', 'convince', 'cook', 'cooker', 'cookie', 'cooking', 'cool', 'cope', 'copy', 'core', 'corner', 'correct', 'correctly', 'cost', 'cottage', 'cotton', 'cough', 'coughing', 'could', 'council', 'count', 'counter', 'country', 'countryside', 'county', 'couple', 'courage', 'course', 'court', 'cousin', 'cover', 'covered', 'covering', 'cow', 'crack', 'cracked', 'craft', 'crash', 'crazy', 'cream', 'create', 'creature', 'credit', 'crime', 'criminal', 'crisis', 'criterion', 'critical', 'criticism', 'criticize', 'cross', 'crowd', 'crowded', 'crown', 'crucial', 'cruel', 'crush', 'cry', 'cultural', 'culture', 'cup', 'cupboard', 'curb', 'cure', 'curious', 'curiously', 'curl', 'curly', 'current', 'currently', 'curtain', 'curve', 'curved', 'custom', 'customer', 'customs', 'cut', 'cycle', 'cycling']
         d=['daily', 'damage', 'damp', 'dance', 'dancer', 'dancing', 'danger', 'dangerous', 'dare', 'dark', 'data', 'date', 'daughter', 'day', 'dead', 'deaf', 'deal', 'dear','dean','death', 'debate', 'debt', 'decade', 'decay', 'december', 'decide', 'decision', 'declare', 'decline', 'decorate', 'decoration', 'decorative', 'decrease', 'deep', 'deeply', 'defeat', 'defence', 'defend', 'define', 'definite', 'definitely', 'definition', 'degree', 'delay', 'deliberate', 'deliberately', 'delicate', 'delight', 'delighted', 'deliver', 'delivery', 'demand', 'demonstrate', 'deny', 'department', 'departure', 'depend', 'deposit', 'depress', 'depressed', 'depressing', 'depth', 'derive', 'describe', 'description', 'desert', 'desert', 'deserted', 'deserve', 'design', 'desire', 'desk', 'desperate', 'desperately', 'despite', 'destroy', 'destruction', 'detail', 'detailed', 'determination', 'determine', 'determined', 'develop', 'development', 'device', 'devote', 'devoted', 'diagram', 'diamond', 'diary', 'dictionary', 'die', 'diet', 'difference', 'different', 'differently', 'difficult', 'difficulty', 'dig', 'digital', 'dinner', 'direct', 'direction', 'directly', 'director', 'dirt', 'dirty', 'disabled', 'disadvantage', 'disagree', 'disagreement', 'disappear', 'disappoint', 'disappointed', 'disappointing', 'disappointment', 'disapproval', 'disapprove', 'disapproving', 'disaster', 'disc', 'discipline', 'discount', 'discover', 'discovery', 'discuss', 'discussion', 'disease', 'disgust', 'disgusted', 'disgusting', 'dish', 'dishonest', 'dishonestly', 'disk', 'dislike', 'dismiss', 'display', 'dissolve', 'distance', 'distinguish', 'distribute', 'distribution', 'district', 'disturb', 'disturbing', 'divide', 'division', 'divorce', 'divorced', 'doctor', 'document', 'dog', 'dollar', 'domestic', 'dominate', 'door', 'dot', 'double', 'doubt', 'down', 'downstairs', 'downward', 'downwards', 'dozen', 'draft', 'drag', 'drama', 'dramatic', 'dramatically', 'draw', 'drawer', 'drawing', 'dream', 'dress', 'dressed', 'drink', 'drive', 'driver', 'driving', 'drop', 'drugstore', 'drum', 'drunk', 'dry', 'due', 'dull', 'dump', 'during', 'duty', 'dvd', 'dying']
         e=['each', 'ear', 'early', 'earn', 'earth', 'ease', 'easily', 'east', 'eastern', 'easy', 'eat', 'economic', 'economy', 'edge', 'edition', 'editor', 'educate', 'educated', 'education', 'effect', 'effective', 'effectively', 'efficient', 'efficiently', 'effort', 'egg', 'eight', 'eighteen', 'eighteenth', 'eighth', 'eightieth', 'eighty', 'either', 'elbow', 'elderly', 'elect', 'election', 'electric', 'electrical', 'electricity', 'electronic', 'elegant', 'element', 'elevator', 'eleven', 'eleventh', 'else', 'elsewhere', 'email', 'embarrass', 'embarrassed', 'embarrassing', 'embarrassment', 'emerge', 'emergency', 'emotion', 'emotional', 'emotionally', 'emphasis', 'emphasize', 'empire', 'employ', 'employee', 'employer', 'employment', 'empty', 'enable', 'encounter', 'encourage', 'encouragement', 'end', 'ending', 'enemy', 'energy', 'engage', 'engaged', 'engine', 'engineer', 'engineering', 'enjoy', 'enjoyable', 'enjoyment', 'enormous', 'enough', 'enquiry', 'ensure', 'enter', 'entertain', 'entertainer', 'entertaining', 'entertainment', 'enthusiasm', 'enthusiastic', 'enthusiastically', 'entire', 'entirely', 'entitle', 'entry', 'envelope', 'environment', 'environmental', 'equal', 'equally', 'equipment', 'equivalent', 'error', 'escape', 'especially', 'essay', 'essential', 'essentially', 'establish', 'estate', 'estimate', 'euro', 'even', 'evening', 'event', 'eventually', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'evidence', 'evil', 'exact', 'exactly', 'exaggerate', 'exaggerated', 'exam', 'examination', 'examine', 'example', 'excellent', 'except', 'exception', 'exchange', 'excite', 'excited', 'excitement', 'exciting', 'exclude', 'excluding', 'excuse', 'excuse', 'executive', 'exercise', 'exhibit', 'exhibition', 'exist', 'existence', 'exit', 'expand', 'expect', 'expectation', 'expected', 'expense', 'expensive', 'experience', 'experienced', 'experiment', 'expert', 'explain', 'explanation', 'explode', 'explore', 'explosion', 'export', 'export', 'expose', 'express', 'expression', 'extend', 'extension', 'extensive', 'extent', 'extra', 'extraordinary', 'extreme', 'extremely', 'eye']
         f=['face', 'facility', 'fact', 'factor', 'factory', 'fail', 'failure', 'faint', 'faintly', 'fair', 'fairly', 'faith', 'faithful', 'faithfully', 'fall', 'false', 'fame', 'familiar', 'family', 'famous', 'fan', 'fancy', 'far', 'farm', 'farmer', 'farming', 'farther', 'farthest', 'fashion', 'fashionable', 'fast', 'fasten', 'fat', 'father', 'faucet', 'fault', 'favour', 'favourite', 'fear', 'feather', 'feature', 'february', 'federal', 'fee', 'feed', 'feel', 'feeling', 'fellow', 'female', 'fence', 'festival', 'fetch', 'fever', 'few', 'field', 'fifteen', 'fifteenth', 'fifth', 'fiftieth', 'fifty', 'fight', 'fighting', 'figure', 'file', 'fill', 'film', 'final', 'finally', 'finance', 'financial', 'find', 'fine', 'finely', 'finger', 'finish', 'finished', 'fire', 'firm', 'firmly', 'first', 'fish', 'fishing', 'fit', 'five', 'fix', 'fixed', 'flag', 'flame', 'flash', 'flat', 'flavour', 'flesh', 'flight', 'float', 'flood', 'flooded', 'flooding', 'floor', 'flour', 'flow', 'flower', 'flu', 'fly', 'flying', 'focus', 'fold', 'folding', 'follow', 'following', 'food', 'foot', 'football', 'for', 'force', 'forecast', 'foreign', 'forest', 'forever', 'forget', 'forgive', 'fork', 'form', 'formal', 'formally', 'former', 'formerly', 'formula', 'fortieth', 'fortune', 'forty', 'forward', 'found', 'foundation', 'four', 'fourteen', 'fourteenth', 'fourth', 'frame', 'free', 'freedom', 'freely', 'freeze', 'frequent', 'frequently', 'fresh', 'freshly', 'friday', 'fridge', 'friend', 'friendly', 'friendship', 'frighten', 'frightened', 'frightening', 'from', 'front', 'frozen', 'fruit', 'fry', 'fuel', 'full', 'fully', 'fun', 'function', 'fund', 'fundamental', 'funeral', 'funny', 'fur', 'furniture', 'further', 'future']
         g=['gain', 'gallon', 'gamble', 'gambling', 'game', 'gap', 'garage', 'garbage', 'garden', 'gas', 'gasoline', 'gate', 'gather', 'gear', 'gender','general', 'generally', 'generate', 'generation', 'generous', 'generously', 'gentle', 'gentleman', 'gently', 'genuine', 'genuinely', 'geography', 'get', 'giant', 'gift', 'girl', 'girlfriend', 'give', 'glad', 'glass', 'global', 'glove', 'glue', 'go', 'goal', 'god', 'gold', 'good', 'goodbye', 'goods', 'govern', 'government', 'governor', 'grab', 'grade', 'gradual', 'gradually', 'grain', 'gram', 'grammar', 'grand', 'grandchild', 'granddaughter', 'grandfather', 'grandmother', 'grandparent', 'grandson', 'grant', 'grass', 'grateful', 'gravely', 'great', 'greatly', 'grey', 'grocery', 'ground', 'group', 'grow', 'growth', 'guarantee', 'guard', 'guess', 'guest', 'guide', 'guilty', 'gun', 'guy']
         h=['hop','hut','habit', 'hair', 'hairdresser', 'half', 'hall', 'hammer', 'hand', 'handle', 'hang', 'happen', 'happily', 'happiness', 'happy', 'hard', 'hardly', 'harm', 'harmful', 'harmless', 'hat', 'hate', 'hatred', 'have', 'he', 'head', 'headache', 'heal', 'health', 'healthy', 'hear', 'hearing', 'heart', 'heat', 'heating', 'heaven', 'heavily', 'heavy', 'heel', 'g.heght', 'hell', 'hello', 'help', 'helpful', 'hence', 'her', 'here', 'hero', 'hers', 'herself', 'hesitate', 'hi', 'hide', 'high', 'highlight', 'highly', 'highway', 'hill', 'him', 'himself', 'hip', 'hire', 'his', 'historical', 'history', 'hit', 'hobby', 'hold', 'hole', 'holiday', 'hollow', 'holy', 'home', 'homework', 'honest', 'honestly', 'honour', 'hook', 'hope', 'horizontal', 'horn', 'horror', 'horse', 'hospital', 'host', 'hot', 'hotel', 'hour', 'house', 'household', 'housing', 'how', 'however', 'huge', 'human', 'humorous', 'humour', 'hundred', 'hundredth', 'hungry', 'hunt', 'hunting', 'hurry', 'hurt', 'husband']
         i=['ice','idea', 'ideal', 'identify', 'identity', 'if', 'ignore', 'ill', 'illegal', 'illegally', 'illness', 'illustrate', 'image', 'imaginary', 'imagination', 'imagine', 'immediate', 'immediately', 'immoral', 'impact', 'impatient', 'implication', 'imply', 'import', 'import', 'importance', 'important', 'importantly', 'impose', 'impossible', 'impress', 'impressed', 'impression', 'impressive', 'improve', 'improvement', 'in', 'inability', 'inch', 'incident', 'include', 'including', 'income', 'increase', 'increasingly', 'indeed', 'independence', 'independent', 'independently', 'index', 'indicate', 'indication', 'indirect', 'indirectly', 'individual', 'indoor', 'indoors', 'industrial', 'industry', 'inevitable', 'inevitably', 'infect', 'infected', 'infection', 'infectious', 'influence', 'inform', 'informal', 'information', 'ingredient', 'initial', 'initially', 'initiative', 'injure', 'injured', 'injury', 'ink', 'inner', 'innocent', 'insect', 'insert', 'inside', 'insist', 'install', 'instance', 'instead', 'institute', 'institution', 'instruction', 'instrument', 'insult', 'insulting', 'insurance', 'intelligence', 'intelligent', 'intend', 'intended', 'intention', 'interest', 'interested', 'interesting', 'interior', 'internal', 'international', 'internet', 'interpret', 'interpretation', 'interrupt', 'interruption', 'interval', 'interview', 'into', 'introduce', 'introduction', 'invent', 'invention', 'invest', 'investigate', 'investigation', 'investment', 'invitation', 'invite', 'involve', 'involved', 'involvement', 'iron', 'irritate', 'irritated', 'irritating', 'island', 'issue', 'it', 'item', 'its', 'itself']
         j=['jacket', 'jam', 'january', 'jealous', 'jeans', 'jelly', 'jewellery', 'job', 'join', 'joint', 'jointly', 'joke', 'journalist', 'journey', 'joy', 'judge', 'judgement', 'juice', 'july', 'jump', 'june', 'junior', 'just', 'justice', 'justify', 'justified']
         k=['keen', 'keep', 'key', 'keyboard', 'kick', 'kid', 'kill', 'killing', 'kilogram', 'kilometre', 'kind', 'kindly', 'kindness', 'king', 'kiss', 'kitchen', 'knee', 'knife', 'knit', 'knitted', 'knitting', 'knock', 'knot', 'know', 'knowledge']
         l=['lab','lie', 'label', 'laboratory', 'labour', 'lack', 'lacking', 'lady', 'lake', 'lamp', 'land', 'landscape', 'lane', 'language', 'large', 'largely', 'late', 'later', 'latest', 'latter', 'laugh', 'launch', 'law', 'lawyer', 'lay', 'layer', 'lazy', 'leader', 'leaf', 'league', 'lean', 'learn', 'least', 'leather', 'leave', 'lecture', 'left', 'leg', 'legal', 'legally', 'lemon', 'lend', 'length', 'less', 'lesson', 'let', 'letter', 'level', 'library', 'licence', 'license', 'lid', 'life', 'lift', 'light', 'lightly', 'like', 'likely', 'limit', 'limited', 'line', 'link', 'lip', 'liquid', 'list', 'listen', 'literature', 'litre', 'little', 'live', 'lively', 'living', 'load', 'loan', 'local', 'locally', 'locate', 'located', 'location', 'lock', 'logic', 'logical', 'lonely', 'long', 'look', 'loose', 'loosely', 'lord', 'lorry', 'lose', 'loss', 'lost', 'lot', 'loud', 'loudly', 'love', 'lovely', 'lover', 'low', 'loyal', 'luck', 'lucky', 'luggage', 'lump', 'lunch', 'lung']
         m=['met','mat','machine', 'machinery', 'mad', 'magazine', 'magic', 'mail', 'main', 'mainly', 'maintain', 'major', 'majority', 'make', 'male', 'mall', 'man', 'manage', 'management', 'manager', 'manner', 'manufacture', 'manufacturer', 'manufacturing', 'many', 'map', 'march', 'march', 'mark', 'market', 'marketing', 'marriage', 'married', 'marry', 'mass', 'massive', 'master', 'match', 'matching', 'mate', 'material', 'mathematics', 'matter', 'maximum', 'may', 'may', 'maybe', 'mayor', 'me', 'meal', 'mean', 'meaning', 'means', 'meanwhile', 'measure', 'measurement', 'meat', 'media', 'medical', 'medicine', 'medium', 'meet', 'meeting', 'melt', 'member', 'membership', 'memory', 'mental', 'mentally', 'mention', 'menu', 'mere', 'merely', 'mess', 'message', 'metal', 'method', 'metre', 'midday', 'middle', 'midnight', 'might', 'mild', 'mile', 'military', 'milk', 'milligram', 'millimetre', 'million', 'millionth', 'mind', 'mine', 'mineral', 'minimum', 'minister', 'ministry', 'minor', 'minority', 'mirror', 'miss', 'missing', 'mistake', 'mistaken', 'mix', 'mixed', 'mixture', 'mobile', 'model', 'modern', 'mom', 'moment', 'monday', 'money', 'monitor', 'month', 'mood', 'moon', 'moral', 'morally', 'more', 'moreover', 'morning', 'most', 'mostly', 'mother', 'motion', 'motor', 'motorbike', 'motorcycle', 'mount', 'mountain', 'mouse', 'mouth', 'move', 'movement', 'movie', 'moving', 'much', 'mud', 'multiply', 'mum', 'murder', 'muscle', 'museum', 'music', 'musical', 'musician', 'must', 'my', 'myself', 'myster', 'mysterious']
         n=['nail', 'naked', 'name', 'narrow', 'nation', 'national', 'natural', 'naturally', 'nature', 'near', 'nearby', 'nearly', 'neat', 'neatly', 'necessarily', 'necessary', 'neck', 'need', 'needle', 'negative', 'neighbour', 'neighbourhood', 'neither', 'nephew', 'nerve', 'nervous', 'nervously', 'nest', 'net', 'network', 'never', 'nevertheless', 'new', 'newly', 'news', 'newspaper', 'next', 'nice', 'nicely', 'niece', 'night', 'nine', 'nineteen', 'nineteenth', 'ninetieth', 'ninety', 'ninth', 'no', 'nobody', 'noise', 'noisily', 'noisy', 'none', 'nonsense', 'nor', 'normal', 'normally', 'north', 'northern', 'nose', 'not', 'note', 'nothing', 'notice', 'noticeable', 'novel', 'november', 'now', 'nowhere', 'nut', 'nuclear', 'number', 'nurse']
         o=['obey', 'object', 'object', 'objective', 'observation', 'observe', 'obtain', 'obvious', 'obviously', 'occasion', 'occasionally', 'occupied', 'occupy', 'occur', 'ocean', 'october', 'odd', 'oddly', 'of', 'off', 'offence', 'offend', 'offense', 'offensive', 'offer', 'office', 'officer', 'official', 'officially', 'often', 'oh', 'oil', 'ok', 'old', 'on', 'once', 'one', 'onion', 'online', 'only', 'onto', 'open', 'opening', 'openly', 'operate', 'operation', 'opinion', 'opponent', 'opportunity', 'oppose', 'opposed', 'opposing', 'opposite', 'opposition', 'option', 'or', 'orange', 'order', 'ordinary', 'organ', 'organization', 'organize', 'organized', 'origin', 'original', 'originally', 'other', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'outdoor', 'outdoors', 'outer', 'outline', 'output', 'outside', 'outside', 'outstanding', 'oven', 'over', 'overall', 'overcome', 'owe', 'own', 'owner']
         p=['pack', 'package', 'packaging', 'packet', 'page', 'pain', 'painful', 'paint', 'painter', 'painting', 'pair', 'palace', 'pale', 'panel', 'pants', 'paper', 'parallel', 'parent', 'park', 'parliament', 'part', 'particular', 'particularly', 'partly', 'partner', 'partnership', 'party', 'pass', 'passage', 'passenger', 'passing', 'passport', 'past', 'path', 'patience', 'patient', 'pattern', 'pause', 'pay', 'payment', 'peace', 'peaceful', 'peak', 'pen', 'pencil', 'penny', 'people', 'pepper', 'per', 'perfect', 'perfectly', 'perform', 'performance', 'performer', 'perhaps', 'period', 'permanent', 'permanently', 'permission', 'permit', 'person', 'personal', 'personality', 'personally', 'persuade', 'pet', 'petrol', 'phase', 'philosophy', 'phone', 'photo', 'photocopy', 'photograph', 'photographer', 'photography', 'phrase', 'physical', 'physically', 'physics', 'piano', 'pick', 'picture', 'piece', 'pig', 'pile', 'pill', 'pilot', 'pin', 'pink', 'pint', 'pipe', 'pitch', 'pity', 'place', 'plain', 'plan', 'plane', 'planet', 'planning', 'plant', 'plastic', 'plate', 'platform', 'play', 'player', 'pleasant', 'pleasantly', 'please', 'pleased', 'pleasing', 'pleasure', 'plenty', 'plot', 'plug', 'pocket', 'poem', 'poetry', 'point', 'pointed', 'poison', 'poisonous', 'pole', 'policy', 'polish', 'polite', 'politely', 'political', 'politically', 'politician', 'politics', 'pollution', 'pool', 'poor', 'pop', 'popular', 'population', 'port', 'pose', 'position', 'positive', 'possess', 'possession', 'possibility', 'possible', 'possibly', 'post', 'pot', 'potato', 'potential', 'potentially', 'pound', 'pour', 'powder', 'power', 'powerful', 'practical', 'practically', 'practice', 'practise', 'praise', 'pray', 'prayer', 'precise', 'precisely', 'predict', 'prefer', 'preference', 'pregnant', 'premises', 'preparation', 'prepare', 'prepared', 'presence', 'present', 'present', 'presentation', 'preserve', 'president', 'press', 'pressure', 'presumably', 'pretend', 'pretty', 'prevent', 'previous', 'previously', 'price', 'pride', 'priest', 'primarily', 'primary', 'prince', 'princess', 'principle', 'print', 'printer', 'printing', 'prior', 'priority', 'prison', 'prisoner', 'private', 'privately', 'prize', 'probable', 'probably', 'problem', 'procedure', 'proceed', 'produce', 'producer', 'product', 'production', 'profession', 'professional', 'professor', 'profit', 'program', 'programme', 'progress', 'progress', 'project', 'project', 'promise', 'promote', 'promotion', 'prompt', 'promptly', 'pronounce', 'proof', 'proper', 'properly', 'property', 'proportion', 'proposal', 'propose', 'prospect', 'protect', 'protection', 'protest', 'protest', 'proud', 'proudly', 'prove', 'provide', 'provided', 'providing', 'pub', 'public', 'publication', 'publicity', 'publicly', 'publish', 'publishing', 'pull', 'punch', 'punish', 'punishment', 'pupil', 'purchase', 'pure', 'purely', 'purple', 'purpose', 'pursue', 'push', 'put']
         q=['qualification', 'qualified', 'qualify', 'quality', 'quantity', 'quarter', 'queen', 'question', 'quick', 'quickly', 'quiet', 'quietly', 'quit', 'quite', 'quote']
         r=['rap','race', 'racing', 'radio', 'rail', 'railroad', 'railway', 'rain', 'raise', 'range', 'rank', 'rapid', 'rapidly', 'rare', 'rarely', 'rate', 'rather', 'raw', 'reach', 'react', 'reaction', 'read', 'reader', 'reading', 'ready', 'real', 'realistic', 'reality', 'realize', 'really', 'rear', 'reason', 'reasonable', 'reasonably', 'recall', 'receipt', 'receive', 'recent', 'recently', 'reception', 'reckon', 'recognition', 'recognize', 'recommend', 'record', 'record', 'recording', 'recover', 'red', 'reduce', 'reduction', 'refer', 'reference', 'reflect', 'reform', 'refrigerator', 'refusal', 'regard', 'regarding', 'region', 'regional', 'register', 'regret', 'regular', 'regularly', 'regulation', 'reject', 'relate', 'related', 'relation', 'relationship', 'relative', 'relatively', 'relax', 'relaxed', 'relaxing', 'release', 'relevant', 'relief', 'religion', 'religious', 'rely', 'remain', 'remaining', 'remains', 'remark', 'remarkable', 'remarkably', 'remember', 'remind', 'remote', 'removal', 'remove', 'rent', 'rented', 'repair', 'repeat', 'repeated', 'repeatedly', 'replace', 'reply', 'report', 'represent', 'representative', 'reproduce', 'reputation', 'request', 'require', 'requirement', 'rescue', 'research', 'reservation', 'reserve', 'resident', 'resist', 'resistance', 'resolve', 'resort', 'resource', 'respect', 'respond', 'response', 'responsibility', 'responsible', 'rest', 'restaurant', 'restore', 'restrict', 'restricted', 'restriction', 'result', 'retain', 'retire', 'retired', 'retirement', 'return', 'reveal', 'reverse', 'review', 'revise', 'revision', 'revolution', 'reward', 'rhythm', 'rice', 'rich', 'rid', 'ride', 'rider', 'ridiculous', 'riding', 'right', 'rightly', 'rise', 'risk', 'rival', 'river', 'road', 'rob', 'rock', 'role', 'roll', 'romantic', 'roof', 'room', 'root', 'rope', 'rough', 'roughly', 'round', 'rounded', 'route', 'routine', 'royal', 'rub', 'rubber', 'rubbish', 'rude', 'rudely', 'ruin', 'ruined', 'rule', 'ruler', 'rumour', 'run', 'runner', 'running', 'rural', 'rush']
         s=['sack', 'sad', 'sadly', 'sadness', 'safe', 'safely', 'safety', 'sail', 'sailing', 'sailor', 'salad', 'salary', 'sale', 'salt', 'salty', 'same', 'sample', 'sand', 'satisfaction', 'satisfied', 'satisfy', 'satisfying', 'saturday', 'sauce', 'save', 'saving', 'say', 'scale', 'scare', 'scared', 'scene', 'schedule', 'scheme', 'school', 'science', 'scientific', 'scientist', 'scissors', 'score', 'scratch', 'scream', 'screen', 'screw', 'sea', 'seal', 'search', 'season', 'seat', 'secondary', 'secret', 'secretary', 'secretly', 'section', 'sector', 'secure', 'security', 'see', 'seed', 'seek', 'seem', 'select', 'selection', 'self', 'sell', 'senate', 'senator', 'send', 'senior', 'sense', 'sensible', 'sensitive', 'sentence', 'separate', 'separate', 'separated', 'separately', 'separation', 'september', 'series', 'serious', 'seriously', 'servant', 'serve', 'service', 'session', 'set', 'settle', 'seven', 'seventeen', 'seventh', 'seventieth', 'seventy', 'several', 'severe', 'severely', 'sew', 'sewing', 'shade', 'shadow', 'shake', 'shall', 'shallow', 'shame', 'shape', 'shaped', 'share', 'sharp', 'sharply', 'shave', 'she', 'sheep', 'sheet', 'shelf', 'shell', 'shelter', 'shift', 'shine', 'shiny', 'ship', 'shirt', 'shock', 'shocked', 'shocking', 'shoe', 'shoot', 'shooting', 'shopping', 'short', 'shortly', 'shot', 'should', 'shoulder', 'shout', 'show', 'shower', 'shut', 'shy', 'sick', 'side', 'sideways', 'sight', 'sign', 'signal', 'signature', 'significant', 'significantly', 'silence', 'silent', 'silk', 'silly', 'silver', 'similar', 'similarly', 'simple', 'simply', 'since', 'sincere', 'sincerely', 'sing', 'singer', 'singing', 'single', 'sink', 'sir', 'sister', 'sit', 'site', 'situation', 'six', 'sixteen', 'sixth', 'sixtieth', 'sixty', 'size', 'skilful', 'skilfully', 'skill', 'skilled', 'skin', 'skirt', 'sky', 'sleep', 'sleeve', 'slice', 'slide', 'slight', 'slightly', 'slip', 'slope', 'slow', 'slowly', 'small', 'smart', 'smash', 'smell', 'smile', 'smoke', 'smoking', 'smooth', 'smoothly', 'snake', 'snow', 'so', 'soap', 'social', 'socially', 'society', 'sock', 'soft', 'softly', 'software', 'soil', 'soldier', 'solid', 'solution', 'solve', 'some', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometimes', 'somewhat', 'somewhere', 'son', 'song', 'soon', 'sore', 'sorry', 'sort', 'soul', 'sound', 'soup', 'sour', 'source', 'south', 'southern', 'space', 'spare', 'speak', 'speaker', 'special', 'specialist', 'specially', 'specific', 'specifically', 'speech', 'speed', 'spell', 'spelling', 'spend', 'spice', 'spicy', 'spider', 'spin', 'spirit', 'spiritual', 'spite', 'split', 'spoil', 'spoken', 'spoon', 'sport', 'spot', 'spray', 'spread', 'spring', 'square', 'squeeze', 'stable', 'staff', 'stage', 'stair', 'stamp', 'stand', 'standard', 'star', 'stare', 'start', 'state', 'statement', 'station', 'statue', 'status', 'stay', 'steadily', 'steady', 'steal', 'steam', 'steel', 'steep', 'steeply', 'steer', 'step', 'stick', 'sticky', 'stiff', 'stiffly', 'still', 'sting', 'stir', 'stock', 'stomach', 'stone', 'stop', 'store', 'storm', 'story', 'stove', 'straight', 'strain', 'strange', 'strangely', 'stranger', 'strategy', 'stream', 'street', 'strength', 'stress', 'stressed', 'stretch', 'strict', 'strictly', 'strike', 'striking', 'string', 'strip', 'stripe', 'striped', 'stroke', 'strong', 'strongly', 'structure', 'struggle', 'student', 'studio', 'study', 'stuff', 'stupid', 'style', 'subject', 'substance', 'substantial', 'substantially', 'substitute', 'succeed', 'success', 'successful', 'successfully', 'such', 'suck', 'sudden', 'suddenly','sue', 'suffer', 'suffering', 'sufficient', 'sufficiently', 'sugar', 'suggest', 'suggestion', 'suit', 'suitable', 'suitcase', 'suited', 'sum', 'summary', 'summer', 'sun', 'sunday', 'superior', 'supermarket', 'supply', 'support', 'supporter', 'suppose', 'sure', 'surely', 'surface', 'surname', 'surprise', 'surprised', 'surprising', 'surprisingly', 'surround', 'surrounding', 'survey', 'survey', 'survive', 'suspect', 'suspicion', 'suspicious', 'swallow', 'swear', 'swearing', 'sweat', 'sweater', 'sweep', 'sweet', 'swell', 'swelling', 'swimming', 'swing', 'switch', 'swollen', 'symbol', 'sympathetic', 'sympathy', 'system']
         t=['table', 'tablet', 'tackle', 'tail', 'take', 'talk', 'tall', 'tank', 'tap', 'tape', 'target', 'task', 'taste', 'tax', 'taxi', 'tea', 'teach', 'teacher', 'teaching', 'team', 'technical', 'technique', 'technology', 'telephone', 'television', 'tell', 'temperature', 'temporarily', 'temporary', 'ten', 'tend', 'tendency', 'tension', 'tent', 'tenth', 'term', 'terrible', 'terribly', 'test', 'text', 'than', 'thank', 'thanks', 'that', 'that', 'the', 'theatre', 'them', 'theme', 'themselves', 'then', 'theory', 'there', 'therefore', 'they', 'thick', 'thickly', 'thickness', 'thief', 'thin', 'thing', 'think', 'thinking', 'third', 'thirsty', 'thirteen', 'thirteenth', 'thirtieth', 'thirty', 'this', 'thorough', 'thoroughly', 'though', 'thought', 'thousand', 'thousandth', 'thread', 'threat', 'threaten', 'threatening', 'three', 'throat', 'through', 'throughout', 'throw', 'thumb', 'thursday', 'thus', 'ticket', 'tidy', 'tie', 'tight', 'tightly', 'till', 'time', 'timetable', 'tin', 'tiny', 'tip', 'tire', 'tired', 'tiring', 'title', 'to', 'today', 'toe', 'together', 'toilet', 'tomato', 'tomorrow', 'ton', 'tone', 'tongue', 'tonight', 'tonne', 'too', 'tool', 'tooth', 'top', 'topic', 'total', 'totally', 'touch', 'tough', 'tour', 'tourist', 'towards', 'towel', 'tower', 'town', 'toy', 'trace', 'track', 'trade', 'trading', 'tradition', 'traditional', 'traditionally', 'traffic', 'train', 'training', 'transfer', 'transfer', 'transform', 'translate', 'translation', 'transparent', 'transport', 'transport', 'transportation', 'trap', 'travel', 'traveller', 'treat', 'treatment', 'tree', 'trend', 'trial', 'triangle', 'trick', 'trip', 'tropical', 'trouble', 'trousers', 'truck', 'true', 'truly', 'trust', 'truth', 'try', 'tube', 'tuesday', 'tune', 'tunnel', 'turn', 'tv', 'twelfth', 'twelve', 'twentieth', 'twenty', 'twice', 'twin', 'twist', 'twisted', 'two', 'type', 'typical', 'typically', 'tyre']
         u=['ugly', 'ultimate', 'ultimately', 'umbrella', 'unable', 'unacceptable', 'uncertain', 'uncle', 'uncomfortable', 'unconscious', 'uncontrolled', 'under', 'underground', 'underneath', 'understand', 'understanding', 'underwater', 'underwear', 'undo', 'unemployed', 'unemployment', 'unexpected', 'unexpectedly', 'unfair', 'unfairly', 'unfortunate', 'unfortunately', 'unfriendly', 'unhappy', 'uniform', 'unimportant', 'union', 'unique', 'unit', 'unite', 'united', 'universe', 'university', 'unkind', 'unknown', 'unless', 'unlike', 'unlikely', 'unload', 'unlucky', 'unnecessary', 'unpleasant', 'unreasonable', 'unsteady', 'unsuccessful', 'untidy', 'until', 'unusual', 'unusually', 'unwilling', 'unwillingly', 'up', 'upon', 'upper', 'upset', 'upset', 'upsetting', 'upstairs', 'upward', 'upwards', 'urban', 'urge', 'urgent', 'us', 'use', 'use', 'used', 'useful', 'useless', 'user', 'usual', 'usually']
         v=['vacation', 'valid', 'valley', 'valuable', 'value', 'van', 'variation', 'varied', 'variety', 'various', 'vary', 'vast', 'vegetable', 'vehicle', 'venture', 'version', 'vertical', 'very', 'via', 'victim', 'victory', 'video', 'view', 'village', 'violence', 'violent', 'violently', 'virtually', 'virus', 'visible', 'vision', 'visit', 'visitor', 'vital', 'vocabulary', 'voice', 'volume', 'vote']
         w=['wage', 'waist', 'wait', 'waiter', 'wake', 'walk', 'walking', 'wall', 'wallet', 'wander', 'want', 'war', 'warm', 'warmth', 'warn', 'warning', 'wash', 'washing', 'waste', 'watch', 'water', 'wave', 'way', 'we', 'weak', 'weakness', 'wealth', 'weapon', 'wear', 'weather', 'web', 'website', 'wedding', 'wednesday', 'week', 'weekend', 'weekly', 'weigh', 'weight', 'welcome', 'well', 'west', 'western', 'wet', 'what', 'whatever', 'wheel', 'when', 'whenever', 'where', 'whereas', 'wherever', 'whether', 'which', 'while', 'whisper', 'whistle', 'white', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'wide', 'widely', 'width', 'wife', 'wild', 'wildly', 'will', 'willing', 'willingly', 'willingness', 'win', 'wind', 'window', 'wing', 'winner', 'winning', 'winter', 'wire', 'wise', 'wish', 'with', 'withdraw', 'within', 'without', 'witness', 'woman', 'wonder', 'wonderful', 'wood', 'wooden', 'wool', 'word', 'work', 'worker', 'working', 'world', 'worried', 'worry', 'worrying', 'worse', 'worship', 'worst', 'worth', 'would', 'wounded', 'wrap', 'wrapping', 'wrist', 'write', 'writer', 'writing', 'written', 'wrong']
         y=['yard', 'yawn', 'yeah', 'year', 'yellow', 'yes', 'yesterday', 'yet', 'you', 'young', 'your', 'yours', 'yourself', 'youth']
         z=['zero', 'zone']

         word=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+y+z
         self.d={'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'y':y,'z':z}
         
         

         
         st=""

         num=random.randint(0,3388)
         print(num)
         self.lis.append(word[num])
         st=st+(word[num])
                        
         se=set(st)
         print("lis",self.lis)
         print("set",se)

            
         for letter in st:
             if(letter!='x'):
                li=self.d[letter]
             #print("li",li)
             for wrd in li:
                 #print("wrd",wrd)
                 if set(wrd).issubset(se) and (wrd not in self.lis) :
                     self.lis.append(wrd)
         print(self.lis)
         if((len(se)<4 or len(se)>=8) or ((len(self.lis)<5 or len(self.lis)>10))):
            redo=1
            self.lis=[]
            
         else:
            redo=0
      print(self.lis)

      self.list1=list(se)
      self.len1=len(self.list1)
      print(self.list1,self.len1)
      self.word_found=[1 for i in range(len(self.lis)+1)]
      print(self.word_found)
      self.time_stop=len(self.lis)
      
      
      self.wg=self.wi//self.len1
      self.hg=self.he//2.5
      self.tw=self.wg*(self.len1-2)
      self.th=self.hg*1.5
      self.cw=self.wg*(self.len1-1)
     
      self.tick1=pygame.transform.scale(self.tick1,(int(self.size*2),int(self.size*2)))
      self.cross1=pygame.transform.scale(self.cross1,(int(self.size*2),int(self.size*2)))
      self.disp.blit(self.tick1,(self.tw,self.th))
      self.disp.blit(self.cross1,(self.cw,self.th))
      
      self.clear=pygame.transform.scale(self.clear,(int(self.size*2),int(self.size*2)))
      self.disp.blit(self.clear,(self.tw,self.th+140))
      self.font = pygame.font.SysFont("Times New Roman",30,bold=False,italic=False)
      self.text = self.font.render('CLEAR', True, self.blue)
      self.disp.blit(self.text,[self.tw,(self.th+180)])

      font1 = pygame.font.SysFont('Sans', 50)

      
      for i in range(0,self.len1):
         var=pygame.image.load(di+self.list1[i]+'.png')
         j=i+0.3
         self.x1.append(self.wg*j)
         self.y1.append(self.hg)
         
         #pygame.draw.rect(self.disp,self.yellow,((self.x1[i]-self.size),self.h//3,self.size,self.size))
         #self.button1=pygame.transform.scale(self.button1,(int(self.x1[i]),int(self.x1[i])))
         self.button1=pygame.transform.scale(self.button1,(int(self.size*2),int(self.size*2)))
         var=pygame.transform.scale(var,(int(self.size),int(self.size)))
         #self.disp.blit(self.button1,(self.x1[i]-self.size,self.h//3))
         self.disp.blit(self.button1,(self.x1[i],self.y1[i]))
         self.disp.blit(var,((self.x1[i])+self.size*0.4,self.y1[i]+(self.size*0.5)))
         pygame.display.update()

         text = font1.render(str(self.list1[i-1]), True, (255, 0, 0))
         #self.sprite.img.blit(text, rect)
         #self.message(str(self.list1[i-1]),self.red,int(self.size)//2,int(self.size)*1.5,self.size)
      self.brain=pygame.transform.scale(self.brain,(int(self.size*1.5),int(self.size*1.5)))
      self.textbox=pygame.transform.scale(self.textbox,(int(self.size*5),int(self.size*5)))
      self.textbox2=pygame.transform.scale(self.textbox2,(int(self.size*4),int(self.size*4)))

      self.disp.blit(self.brain,(0,self.he*0.90))
      self.disp.blit(self.textbox,(0,self.he*0.6))
      #self.disp.blit(self.textbox2,(0,0))
      pygame.display.update()
      print(self.x1,self.y1)
      return

   def write(self,m,x,y):
      pr=pygame.image.load(di+m+'.png')
      pr=pygame.transform.scale(pr,(int(self.size)//2,int(self.size)//2))
      
      self.disp.blit(pr,(x,y))
      
      '''self.font = pygame.font.SysFont("Times New Roman",50,bold=False,italic=False)
      self.text = self.font.render(m, True, g.yellow)
      self.disp.blit(self.text,[x,y]) '''     
      pygame.display.update()  
      

   def check(self,st):
      print(self.word_found)      
      if st in self.lis:
         if self.word_found[self.lis.index(st)]:
            self.word_found[self.lis.index(st)]=0
            return 1
         else:
            return 2
      return 0

      pygame.display.update()
      
   def timer(self):
      
      t=time.asctime( time.localtime(time.time()) )[14:19]
      self.mi=int(t[0:2])
      self.sec=int(t[3:])
      self.mi=self.mi+self.time_stop
      print(self.mi,self.sec)

      pygame.display.update()  

g=game()


g.message("WORD GAME",g.purple,70,80,g.size*2)

but1=pygame.image.load(di+'square-butt-1.png')
but2=pygame.image.load(di+'square-butt-3.png')
button3=pygame.image.load(di+'button-select.png')
but1=pygame.transform.scale(but1,(int(g.size*4),int(g.size*4)))
g.disp.blit(but1,(g.size,g.he//3))
g.disp.blit(but1,(g.size*10,g.he//3))
g.disp.blit(but1,(g.size*20,g.he//3))

g.font = pygame.font.SysFont("Times New Roman",50,bold=False,italic=False)
g.text = g.font.render('PLAY', True, g.white)
g.disp.blit(g.text,[g.size*1.8,g.he//2.3])
g.text = g.font.render('RULES', True, g.white)
g.disp.blit(g.text,[g.size*10.5,g.he//2.3])
g.text = g.font.render('EXIT', True, g.white)
g.disp.blit(g.text,[g.size*20.7,g.he//2.3])

#g.disp.blit(var,((self.x1[i])+self.size*0.4,self.y1[i]+(self.size*0.5)))
#g.message("CHOOSE THE GAME U WANT TO PLAY",g.red,0,0,g.size)
#pygame.gfxdraw.circle(g.disp, 100, 200, 100, g.red)
siz=g.size*2
siz2=g.size*4
siz3=g.size*6
c=10
word_count=0

wrd=[]
'''pygame.draw.circle(g.disp,g.red,[siz,siz2],siz,0)
g.message("PLAY",g.blue,siz//2.8,siz2,g.size//2)'''
but=[0 for i in range(26)]
pygame.display.update()

while not g.gameExit:
    x=0
    if g.gameStatus==1:
       t=time.asctime(time.localtime(time.time()))[14:19]
       min1=int(t[0:2])
       sec1=int(t[3:])
       #print(min1,sec1)
       diff_s=g1.sec-sec1
       diff_m=g1.mi-min1
       #print(diff_m,diff_s)



       if diff_s<0:
          diff_s=60+diff_s
          diff_m=diff_m-1

       pygame.draw.rect(g.disp,g.white,(g1.tw+50,30,int(g.size)*10,int(g.size)*5))
       t1='Time Left - '+str(diff_m)+':'+str(diff_s)
          
       if diff_m==0 and diff_s==0:
          t1='Time elapsed'
          print('gameover')
          g.gameStatus=3
       tim = g.font.render(t1, True, g.blue)
       g.disp.blit(tim,[g1.tw*1.1,30])
       pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or g.gameStatus==3:
            g.gameExit = True
        elif event.type == pygame.KEYDOWN:
           if(event.key==pygame.K_ESCAPE):
              g.gameExit = True              

       

           
        if g.gameStatus==0 and event.type==pygame.MOUSEMOTION:
           posi=pygame.mouse.get_pos()
           x=posi[0]
           y=posi[1]
           if (g.size<=x<=g.size+int(g.size*4) and g.he//4<=y<=g.he//4+int(g.size*4)):               
              but2=pygame.transform.scale(but2,(int(g.size*4),int(g.size*4)))
              g.disp.blit(but2,(g.size,g.he//3))
              g.text = g.font.render('PLAY', True, g.purple)
              g.disp.blit(g.text,[g.size*1.8,g.he//2.3])
              pygame.display.update()
           else:
              but1=pygame.transform.scale(but1,(int(g.size*4),int(g.size*4)))
              g.disp.blit(but1,(g.size,g.he//3))
              g.text = g.font.render('PLAY', True, g.white)
              g.disp.blit(g.text,[g.size*1.8,g.he//2.3])
              pygame.display.update()

           if(g.size*10<=x<=g.size*10+int(g.size*4) and g.he//4<=y<=g.he//4+int(g.size*4)):
              but2=pygame.transform.scale(but2,(int(g.size*4),int(g.size*4)))
              g.disp.blit(but2,(g.size*10,g.he//3))
              g.text = g.font.render('RULES', True, g.purple)
              g.disp.blit(g.text,[g.size*10.5,g.he//2.3])
              pygame.display.update()
            
           else:
              but1=pygame.transform.scale(but1,(int(g.size*4),int(g.size*4)))
              g.disp.blit(but1,(g.size*10,g.he//3))
              g.text = g.font.render('RULES', True, g.white)
              g.disp.blit(g.text,[g.size*10.5,g.he//2.3])
              pygame.display.update()
           if(g.size*20<=x<=g.size*20+int(g.size*4) and g.he//4<=y<=g.he//4+int(g.size*4)):
              but2=pygame.transform.scale(but2,(int(g.size*4),int(g.size*4)))
              g.disp.blit(but2,(g.size*20,g.he//3))
              g.text = g.font.render('EXIT', True, g.purple)
              g.disp.blit(g.text,[g.size*20.7,g.he//2.3])
              pygame.display.update()
           else:
              but1=pygame.transform.scale(but1,(int(g.size*4),int(g.size*4)))
              g.disp.blit(but1,(g.size*20,g.he//3))
              g.text = g.font.render('EXIT', True, g.white)
              g.disp.blit(g.text,[g.size*20.7,g.he//2.3])
              pygame.display.update()


        if (g.gameStatus==0 and pygame.mouse.get_pressed()[0]==1):
           print('press')

           positio=pygame.mouse.get_pos()
           x=positio[0]
           y=positio[1]

           if (g.size<=x<=g.size+int(g.size*4) and g.he//4<=y<=g.he//4+int(g.size*4)):
              
              g1=wordgame()
              g1.start()
              g1.timer()
              pygame.draw.rect(g.disp,g.white,(10,g1.he*0.7,int(g.size*4.3),int(g.size//2)))
              g.gameStatus=1
              
              
           elif(g.size*10<=x<=g.size*10+int(g.size*4) and g.he//4<=y<=g.he//4+int(g.size*4)):
              g.rule()
              g1=wordgame()
              g1.start()
              g1.timer()
              g.gameStatus=1
              pygame.display.update()
           elif(g.size*20<=x<=g.size*20+int(g.size*4) and g.he//4<=y<=g.he//4+int(g.size*4)):
              pygame.quit()




        if g.gameStatus==1 and event.type==pygame.MOUSEMOTION:

        
           posi1=pygame.mouse.get_pos()
           x=posi1[0]
           y=posi1[1]
           if(g1.tw<=x<=g1.tw+(g.size*2)) and (g1.th<=y<=g1.th+(g.size*2)):
              pygame.draw.rect(g.disp,g.white,(g1.tw,g1.th,int(g.size*2),int(g.size*2)))
              g1.tick2=pygame.transform.scale(g1.tick2,(int(g.size*1.8),int(g.size*1.8)))
              g1.disp.blit(g1.tick2,(g1.tw+0.5,g1.th+0.5))              

              pygame.display.update()
           else:
              pygame.draw.rect(g.disp,g.white,(g1.tw,g1.th,int(g.size*2),int(g.size*2)))
              g1.tick1=pygame.transform.scale(g1.tick1,(int(g.size*2),int(g.size*2)))
              g1.disp.blit(g1.tick1,(g1.tw,g1.th))              

              pygame.display.update()                 
           if(g1.cw<=x<=g1.cw+(g.size*2)) and (g1.th<=y<=g1.th+(g.size*2)):
              pygame.draw.rect(g.disp,g.white,(g1.cw,g1.th,int(g.size*2),int(g.size*2)))
              g1.cross2=pygame.transform.scale(g1.cross2,(int(g.size*1.8),int(g.size*1.8)))
              g1.disp.blit(g1.cross2,(g1.cw+0.5,g1.th+0.5))                    

              pygame.display.update()

           else:
              pygame.draw.rect(g.disp,g.white,(g1.cw,g1.th,int(g.size*2),int(g.size*2)))
              g1.cross1=pygame.transform.scale(g1.cross1,(int(g.size*2),int(g.size*2)))
              g1.disp.blit(g1.cross1,(g1.cw,g1.th))                    

              pygame.display.update()   

           for i in range(g1.len1):
              var=pygame.image.load(di+g1.list1[i]+'.png')
            
              
              if((g1.x1[i])<=x<=g1.x1[i]+(g.size*2) and (g1.y1[i])<=y<=g1.y1[i]+(g.size*2)):
                 
                 pygame.draw.rect(g.disp,g.white,(g1.x1[i],g1.y1[i],siz,siz))
                 g.button3=pygame.transform.scale(g.button3,(int(siz),int(siz)))
                 var=pygame.transform.scale(var,(int(g.size),int(g.size)))
                 g1.disp.blit(g.button3,(g1.x1[i],g1.y1[i]))
                 g1.disp.blit(var,((g1.x1[i])+g.size*0.4,g1.y1[i]+g.size*0.5))
                 pygame.display.update()
                 
                 
              else:

                 pygame.draw.rect(g.disp,g.white,(g1.x1[i],g1.y1[i],siz,siz))
                 g.button1=pygame.transform.scale(g.button1,(int(siz),int(siz)))
                 var=pygame.transform.scale(var,(int(g.size),int(g.size)))
                 g1.disp.blit(g.button1,(g1.x1[i],g1.y1[i]))
                 g1.disp.blit(var,((g1.x1[i])+g.size*0.4,g1.y1[i]+g.size*0.5))
                 pygame.display.update()

        

                               
        if (g.gameStatus==1 and pygame.mouse.get_pressed()[0]==1):
           pos2=pygame.mouse.get_pos()
           x=pos2[0]
           y=pos2[1]
           if(g1.tw<=x<=g1.tw+(g.size*2)) and (g1.th<=y<=g1.th+(g.size*2)):
              word=''
              co=len(g1.lis)
              word=word.join(wrd)
              chk=g1.check(word)
              if(chk==1):
                 print('word matched')
                 pygame.draw.rect(g.disp,g.white,(30,80,g.wi,g.size*3))
                 word_count=word_count+1
                 st=str(word_count)+' / '+str(co)+' words you have found'
                 g.message(st,g.navyblue,70,130,g.size)
                 g.message("WOW U FOUND THE RIGHT WORD",g.red,30,80,g.size)
              elif(chk==2):
                 print('U HAVE ALREADY FOUND IT')
                 pygame.draw.rect(g.disp,g.white,(30,80,g.wi,g.size*3))
                 st=str(word_count)+' / '+str(co)+' words you have found'
                 g.message(st,g.navyblue,70,130,g.size)
                 g.message("U HAVE ALREADY FOUND IT",g.red,30,80,g.size)
              elif(chk==0):
                 print('Sorry')
                 pygame.draw.rect(g.disp,g.white,(30,80,g.wi,g.size*3))
                 st=str(word_count)+' / '+str(co)+' words you have found'
                 g.message(st,g.navyblue,70,130,g.size)
                 g.message("SORRY U MISSED IT",g.red,30,80,g.size)
              if(word_count==co):
                 print('GAME OVER')
                 pygame.draw.rect(g.disp,g.white,(70,80,g.wi,g.size))
                 st=str(word_count)+' / '+str(co)+' words you have found'
                 g.message(st,g.navyblue,70,130,g.size)
            
                 g.message("GAME OVER",g.red,30,80,g.size)
                 
                 pygame.display.update()   
                 #pygame.time.delay(1000000)
                 g.gameStatus=3

              print(word)                  
              print(wrd)
              
         

            
           if(g1.cw<=x<=g1.cw+(g.size*2)) and (g1.th<=y<=g1.th+(g.size*2)):
              c1=c
              c=c-20
              
              word=''
              if(len(wrd)!=0):
                 pygame.draw.rect(g.disp,g.white,(c1-14.5,g1.he*0.7,int(g.size)//2.6,int(g.size*1.3)))
                 wrd.pop()
              word=word.join(wrd)
              #word=word[:-2]
              print(word)                  
              print(wrd)
              pygame.display.update() 

           if(g1.tw<=x<=g1.tw+(g.size*2)) and (g1.th+140<=y<=g1.th+(g.size*2)+140):
              print('hiis')
              word=''
              wrd=[]
              c=10

              pygame.draw.rect(g.disp,g.white,(10,g1.he*0.7,int(g.size*4.3),int(g.size//2)))

              pygame.display.update() 


           for i in range(g1.len1):

              button=g.button3               
              var=pygame.image.load(di+g1.list1[i]+'.png')
              if((c>=10 and c<g.size*4)):

                 #and c<int(g.size*6.5)
   
                 if ((g1.x1[i])<=x<=g1.x1[i]+(g.size*2) and (g1.y1[i])<=y<=g1.y1[i]+(g.size*2)):
 
                    g1.write(str(g1.list1[i]),c,g1.he*0.7)
                    wrd.append(str(g1.list1[i]))
                    c=c+20
                    print(c)
                    #g.message(str(g1.list1[i]),g.navyblue,0.1*i,g1.he*0.95,g.size//2)
                    but[i]=(but[i]+1)%2
                    pygame.display.update()
            
      


  

                 
                 
              
              
if(word_count!=0 and word_count!=len(g1.lis)):
   

   k=2
   g.disp.fill(g.white)
   g.message("WORDS YOU HAVE MISSED OUT:",g.blue,70,80,g.size//2)
   pygame.display.update()
   pygame.display.update()
   for i in range(co):
      if(g1.word_found[i]==1):
         g.message(g1.lis[i],g.green,70,80*k,g.size//2)
         pygame.display.update()
         k=k+1
       
pygame.time.delay(100000)     
       

pygame.quit()



