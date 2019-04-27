from app.model import hack_vigenere, hack_caesar
from app.encode import vigenere
from tests.models import caesar_model, vigenere_model


def test_caesar_short():
    """There are two different algorithms for short and long strings"""
    assert hack_caesar('Hello', caesar_model) == 0


def test_caesar_long():
    """There are two different algorithms for short and long strings"""
    assert hack_caesar(
        '''Canst thou, O cruel! say I love thee not,
When I against myself with thee partake?
Do I not think on thee, when I forgot
Am of my self, all tyrant, for thy sake?
Who hateth thee that I do call my friend,
On whom frown'st thou that I do fawn upon,
Nay, if thou lour'st on me, do I not spend
Revenge upon myself with present moan?
What merit do I in my self respect,
That is so proud thy service to despise,
When all my best doth worship thy defect,
Commanded by the motion of thine eyes?
  But, love, hate on, for now I know thy mind,;
  Those that can see thou lov'st, and I am blind.

CL

O! from what power hast thou this powerful might,
With insufficiency my heart to sway?
To make me give the lie to my true sight,
And swear that brightness doth not grace the day?
Whence hast thou this becoming of things ill,
That in the very refuse of thy deeds
There is such strength and warrantise of skill,
That, in my mind, thy worst all best exceeds?
Who taught thee how to make me love thee more,
The more I hear and see just cause of hate?
O! though I love what others do abhor,
With others thou shouldst not abhor my state:
  If thy unworthiness rais'd love in me,
  More worthy I to be belov'd of thee.

CLI

Love is too young to know what conscience is, 
Yet who knows not conscience is born of love?
Then, gentle cheater, urge not my amiss,
Lest guilty of my faults thy sweet self prove:
For, thou betraying me, I do betray
My nobler part to my gross body's treason;
My soul doth tell my body that he may
Triumph in love; flesh stays no farther reason,
But rising at thy name doth point out thee,
As his triumphant prize. Proud of this pride,
He is contented thy poor drudge to be,
To stand in thy affairs, fall by thy side.
  No want of conscience hold it that I call
  Her 'love,' for whose dear love I rise and fall.

CLII

In loving thee thou know'st I am forsworn,
But thou art twice forsworn, to me love swearing;
In act thy bed-vow broke, and new faith torn,
In vowing new hate after new love bearing:
But why of two oaths' breach do I accuse thee, 
When I break twenty? I am perjur'd most;
For all my vows are oaths but to misuse thee,
And all my honest faith in thee is lost:
For I have sworn deep oaths of thy deep kindness,
Oaths of thy love, thy truth, thy constancy;
And, to enlighten thee, gave eyes to blindness,
Or made them swear against the thing they see;
  For I have sworn thee fair; more perjur'd I,
  To swear against the truth so foul a lie.!
''', caesar_model) == 0


def test_vigenere():
    """There is need to be large test to work properly"""
    assert hack_vigenere(vigenere(
        '''From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And tender churl mak'st waste in niggarding:
  Pity the world, or else this glutton be,
  To eat the world's due, by the grave and thee.

II

When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty's field,
Thy youth's proud livery so gazed on now,
Will be a tatter'd weed of small worth held: 
Then being asked, where all thy beauty lies,
Where all the treasure of thy lusty days; 
To say, within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserv'd thy beauty's use,
If thou couldst answer 'This fair child of mine
Shall sum my count, and make my old excuse,'
Proving his beauty by succession thine!
  This were to be new made when thou art old,
  And see thy blood warm when thou feel'st it cold.
''',
        'abc'),
        vigenere_model) == 'abc'
