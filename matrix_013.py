# Les bases du python / math
# Les collections. 8. Rappelle
from optparse import OptionParser
import sys


# 1. 
# F.A.C.S = Facial Action Coding System
#         = est une methode de description des mouvements du visage
#           developpee par les psychologues Paul Ekman et Wallace Friesen
# (rien a voir avec Python ;-)
#
# T'as un dict des dicts:
dict_au = {  0 : {'name' : 'Neutral face',      'muscles' : 'pas de muscles qui travaillent'     },
             1 : {'name' : 'Inner Brow Raiser', 'muscles' : 'frontalis (pars medialis)'          },
             2 : {'name' : 'Outer Brow Raiser', 'muscles' : 'frontalis (pars lateralis)'         },
             4 : {'name' : 'Brow Lowerer'     ,      'muscles' : 'depressor glabellae, depressor supercilii, corrugator supercilii'},
             5 : {'name' : 'Upper Lid Raiser' , 'muscles' : 'levator palpebrae superioris, superior tarsal muscle'},
             6 : {'name' : 'Cheek Raiser'     ,      'muscles' : 'orbicularis oculi (pars orbitalis)' },
             7 : {'name' : 'Lid Tightener'    , 'muscles' : 'orbicularis oculi (pars palpebralis)' },
             8 : {'name' : 'Lips Toward Each Other' , 'muscles' : 'orbicularis oris' },
             9 : {'name' : 'Nose Wrinkler'    , 'muscles' : 'levator labii superioris alaeque nasi' },
            10 : {'name' : 'Upper Lip Raiser' , 'muscles' : 'levator labii superioris, caput infraorbitalis' },
            11 : {'name' : 'Nasolabial Deepener' , 'muscles' : 'zygomaticus minor' },
            12 : {'name' : 'Lip Corner Puller', 'muscles' : 'zygomaticus major'                  },
            13 : {'name' : 'Sharp Lip Puller' , 'muscles' : 'levator anguli oris (also known as caninus)' },
            14 : {'name' : 'Dimpler'          , 'muscles' : 'buccinator' },
            15 : {'name' : 'Lip Corner Depressor' , 'muscles' : 'depressor anguli oris (also known as triangularis)' },
            16 : {'name' : 'Lower Lip Depressor' , 'muscles' : 'depressor labii inferioris' },
            17 : {'name' : 'Chin Raiser'      , 'muscles' : 'mentalis' },
            18 : {'name' : 'Lip Pucker'       , 'muscles' : 'incisivii labii superioris and incisivii labii inferioris' },
            19 : {'name' : 'Tongue Show'      , 'muscles' : '' },
            20 : {'name' : 'Lip Stretcher'    , 'muscles' : 'risorius w/ platysma' },
            21 : {'name' : 'Neck Tightener'   , 'muscles' : 'platysma' },
            22 : {'name' : 'Lip Funneler'     , 'muscles' : 'orbicularis oris' },
            23 : {'name' : 'Lip Tightener'    , 'muscles' : 'orbicularis oris' },
            24 : {'name' : 'Lip Pressor'      , 'muscles' : 'orbicularis oris' },
            25 : {'name' : 'Lips Part'        , 'muscles' : 'depressor labii inferioris, or relaxation of mentalis or orbicularis oris' },
            26 : {'name' : 'Jaw Drop'         , 'muscles' : 'masseter; relaxed temporalis and internal pterygoid' }
          }

emo_happy    = [6, 12]
emo_sad      = [1, 4, 15]
emo_surprise = [1,2,5,26]
emo_fear     = [1, 2, 4, 5, 7, 20, 26]
emo_anger    = [4, 5, 7, 23]
emo_disgust  = [9, 15, 16]
emo_contempt = [12,14]


def get_muscles(emo):
    for au in emo:
        print '  muscle: ', dict_au[au]['muscles']

def emotion2emo(emotion):
    global emo_happy, emo_sad,emo_surprise,emo_fear,emo_anger,emo_disgust,emo_contempt

    if emotion == 'happy':
        return emo_happy
    if emotion == 'sad':
        return emo_sad
    if emotion == 'surprise':
        return emo_surprise
    if emotion == 'fear':
        return emo_fear
    if emotion == 'anger':
        return emo_anger
    if emotion == 'disgust':
        return emo_disgust
    if emotion == 'contempt':
        return emo_contempt
    else:
        return []
        
if __name__ == "__main__":
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option('-e', '--emotion', action='store', dest='emotion', default=None, help='specify an emotion')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    (options, args) = parser.parse_args()

    print 'Requested emotion: ', options.emotion
    emo = emotion2emo(options.emotion)
    print 'Corresponsing emo: ', emo
    get_muscles(emo)
    





