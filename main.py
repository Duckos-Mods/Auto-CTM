import time
import amulet
import random

from amulet.api.chunk import Chunk
from perlin_noise import PerlinNoise
from amulet.utils.world_utils import chunk_coords_to_block_coords
from amulet.api.block import Block

Seed = random.randint(-1233223, 65535)
level = amulet.load_level(input("Enter Path Two World"))
Scale = int(input("Scale Of CTM MUST Be A Power Of 16 ie [16,32,64,128,256,512,1024,2048]"))
ScaleX, ScaleZ = Scale, Scale
LoopAmountOne, LoopAmountTwo = int(ScaleX / 16), int(ScaleZ / 16)
OctaveOneScale = int(input("Input Base Octave (Be Careful can have wacky results)"))


OctaveOne = PerlinNoise(OctaveOneScale, Seed)
OctaveTwo = PerlinNoise(OctaveOneScale * 2, Seed)
OctaveThree = PerlinNoise(OctaveOneScale * 4, Seed)
OctaveFour = PerlinNoise(OctaveOneScale * 8, Seed)

print("Creating Y Axis Array!...")
Start = time.time()
YAxisArray = [ScaleX * ScaleZ]

GrassBlockInit = Block("minecraft", "grass")
DirtBlockInit = Block("minecraft", "dirt")
StoneBlockInit = Block("minecraft", "stone")

(GrassUni, UselessOne, UseLessTwo,) = level.translation_manager.get_version("bedrock", (1, 19, 30)).block.to_universal(GrassBlockInit)
(DirtUni, UselessOne, UseLessTwo,) = level.translation_manager.get_version("bedrock", (1, 19, 30)).block.to_universal(DirtBlockInit)
(StoneUni, UselessOne, UseLessTwo,) = level.translation_manager.get_version("bedrock", (1, 19, 30)).block.to_universal(StoneBlockInit)

GrassBlock = level.block_palette.get_add_block((GrassUni))
DirtBlock = level.block_palette.get_add_block((DirtUni))
StoneBlock = level.block_palette.get_add_block((StoneUni))


def CreateChunkStuff(X,Z):
    for CX in range(16):
         for CZ in range(16):
            CreatedNoisei = OctaveOne([(X + CX) / ScaleX, (Z + CZ) / ScaleZ])
            CreatedNoisei += 0.5 * OctaveTwo([(X + CX) / ScaleX, (Z + CZ) / ScaleZ])
            CreatedNoisei += 0.25 * OctaveThree([(X + CX) / ScaleX, (Z + CZ) / ScaleZ])
            CreatedNoisei += 0.125 * OctaveFour([(X + CX) / ScaleX, (Z + CZ) / ScaleZ])
            CreatedNoisei *= 100
            YAxisArray.append(int(CreatedNoisei))




for XSlide in range(LoopAmountOne):
    for ZSlide in range(LoopAmountTwo):
        X,Z = chunk_coords_to_block_coords(XSlide, ZSlide)
        CreateChunkStuff(X, Z)


Index = 0
for XSlide in range(LoopAmountOne):
    for ZSlide in range(LoopAmountTwo):
        Before = YAxisArray[Index]
        Calc = Before + 5
        YAxisArray[Index] = Calc
        Index += 1
    Index += 240

YAxisArrayCreationTime = int(time.time() - Start)

print("Created Y Axis Array!... It Took " + str(YAxisArrayCreationTime) + " Seconds")
print("Generating Empty Chunks!...")
Start = time.time()

for ChunkScrollX in range(LoopAmountOne):
    for ChunkScrollZ in range(LoopAmountTwo):
        CreatedChunk = Chunk(ChunkScrollX, ChunkScrollZ)
        level.put_chunk(CreatedChunk, "minecraft:overworld")

CreatedChunk.changed = True
level.save()
EmptyingChunksTime = int(time.time() - Start)

print("Generated Empty Chunks!... It Took " + str(EmptyingChunksTime) + " Seconds")
print("Starting Main Generation loop!...")

IndexOfYArray = 0
NegIndexOfYArray = -1

Start = time.time()

for MainSlideX in range(LoopAmountOne):
    for MainSlideZ in range(LoopAmountTwo):
        CreatedNewChunk = Chunk(MainSlideX, MainSlideZ)
        for X in range(16):
            for Z in range(16):
                CreatedNewChunk.blocks[X, YAxisArray[IndexOfYArray], Z] = GrassBlock
                CreatedNewChunk.blocks[X, YAxisArray[IndexOfYArray] - 1, Z] = DirtBlock
                CreatedNewChunk.blocks[X, YAxisArray[IndexOfYArray] - 2, Z] = StoneBlock
                level.put_chunk(CreatedNewChunk, "minecraft:overworld")
                IndexOfYArray += 1


level.save()
level.close()
print("Finished Main Generation Loop!...")
print("In Total This Has Taken " + str(YAxisArrayCreationTime + EmptyingChunksTime + int(time.time() - Start)) + " Seconds")