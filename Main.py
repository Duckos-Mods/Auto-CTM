import amulet
from amulet.api.block import Block
from amulet.utils.world_utils import block_coords_to_chunk_coords
from amulet.api.chunk import Chunk
import random
from perlin_noise import PerlinNoise
import time

start = time.time()



noise1 = PerlinNoise(octaves=12)
noise2 = PerlinNoise(octaves=24)
noise3 = PerlinNoise(octaves=48)
noise4 = PerlinNoise(octaves=24)



level = amulet.load_level("C:\\Users\\pjhnt\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\iwuFY5JuSQE=")

GrassBlockInit = Block("minecraft", "grass")
DirtBlockInit = Block("minecraft", "dirt")
StoneBlockInit = Block("minecraft", "stone")
LogBlockInit = Block("minecraft", "log")
LeaveBlockInit = Block("minecraft", "leaves")
GrassTallBlockInit = Block("minecraft", "tallgrass")

game_version = ("bedrock", (1, 19, 20))
SizeRecX, SizeRecZ = 512, 512


for X in range(int(SizeRecX/16)):
    for Z in range(int(SizeRecZ/16)):
        newChunk = Chunk(X,Z)

        level.put_chunk(newChunk, "minecraft:overworld")

newChunk.changed = True

level.save()

a = (SizeRecX / 16) * (SizeRecZ / 16)
Chunks = 1
for X in range(int(SizeRecX)):
    for Z in range(int(SizeRecZ)):
        MainNoiseMap = noise1([X/SizeRecX, Z/SizeRecZ])
        MainNoiseMap += 0.5 * noise2([X/SizeRecX, Z/SizeRecZ])
        MainNoiseMap += 0.25 * noise3([X/SizeRecX, Z/SizeRecZ])

        MainNoiseMap *= 100


        level.set_version_block(
            X,
            int(MainNoiseMap),
            Z,
            "minecraft:overworld",
            game_version,
            GrassBlockInit,
        )
        level.set_version_block(
            X,
            int(MainNoiseMap) - 1,
            Z,
            "minecraft:overworld",
            game_version,
            DirtBlockInit,
        )
        level.set_version_block(
            X,
            int(MainNoiseMap) - 2,
            Z,
            "minecraft:overworld",
            game_version,
            DirtBlockInit,
        )
        level.set_version_block(
            X,
            int(MainNoiseMap) - 3,
            Z,
            "minecraft:overworld",
            game_version,
            StoneBlockInit,
        )
        if random.randint(1,50) == 3:
            level.set_version_block(
                X,
                int(MainNoiseMap) + 1,
                Z,
                "minecraft:overworld",
                game_version,
                LogBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 2,
                Z,
                "minecraft:overworld",
                game_version,
                LogBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 3,
                Z,
                "minecraft:overworld",
                game_version,
                LogBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 4,
                Z,
                "minecraft:overworld",
                game_version,
                LogBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 5,
                Z,
                "minecraft:overworld",
                game_version,
                LogBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 6,
                Z,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X + 1,
                int(MainNoiseMap) + 5,
                Z ,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X + 1,
                int(MainNoiseMap) + 6,
                Z ,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 5,
                Z + 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 6,
                Z + 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X - 1,
                int(MainNoiseMap) + 5,
                Z,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X - 1,
                int(MainNoiseMap) + 6,
                Z,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 5,
                Z - 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X,
                int(MainNoiseMap) + 6,
                Z - 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X - 1,
                int(MainNoiseMap) + 5,
                Z - 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X - 1,
                int(MainNoiseMap) + 6,
                Z - 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X - 1,
                int(MainNoiseMap) + 5,
                Z + 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X - 1,
                int(MainNoiseMap) + 6,
                Z + 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X + 1,
                int(MainNoiseMap) + 5,
                Z + 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X + 1,
                int(MainNoiseMap) + 6,
                Z + 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
            level.set_version_block(
                X + 1,
                int(MainNoiseMap) + 5,
                Z - 1,
                "minecraft:overworld",
                game_version,
                LeaveBlockInit,
            )
        elif random.randint(1,5) == 2:
            level.set_version_block(
                X,
                int(MainNoiseMap) + 1,
                Z,
                "minecraft:overworld",
                game_version,
                GrassTallBlockInit,
            )




# save and close the world
level.save()
level.close()


end = time.time()
print(end - start)