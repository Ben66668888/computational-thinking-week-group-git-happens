from ben import get_name as get_ben_name
from oumaima import get_name as get_oumaima_name
from yuv import get_name as get_yuv_name
from SihunYou import get_name as get_SihunYou_name

def team_members():
    print("This is Team Git Happens. We are:")
    print(get_ben_name())
    print(get_oumaima_name())
    print(get_yuv_name())
    print(get_SihunYou_name())


team_members()
