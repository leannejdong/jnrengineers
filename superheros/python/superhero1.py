def on_item_interacted_snowball():
    blocks.fill(SNOW,
        pos(-10, -1, -10),
        pos(10, -1, 10),
        FillOperation.REPLACE)
    for index in range(50):
        mobs.spawn(SNOWBALL_PROJECTILE_MOB,
            randpos(pos(-10, 10, -10), pos(10, 10, 10)))
player.on_item_interacted(SNOWBALL, on_item_interacted_snowball)

def on_on_chat():
    for index2 in range(100):
        blocks.place(SAND, randpos(pos(-10, 10, -10), pos(10, 10, 10)))
        blocks.place(ORANGE_CONCRETE_POWDER,
            randpos(pos(-10, 10, -10), pos(10, 10, 10)))
player.on_chat("sand", on_on_chat)

def on_item_interacted_iron_axe():
    for index3 in range(20):
        mobs.spawn(LIGHTNING_BOLT,
            randpos(pos_camera(-5, 0, 5), pos_camera(5, 0, 10)))
player.on_item_interacted(IRON_AXE, on_item_interacted_iron_axe)

def on_item_interacted_kelp():
    blocks.fill(SEA_LANTERN,
        positions.ground_position(pos(-10, 0, -10)),
        positions.ground_position(pos(10, 0, 10)),
        FillOperation.REPLACE)
    blocks.fill(AIR,
        positions.ground_position(pos(-9, 0, -9)),
        positions.ground_position(pos(9, 0, 9)),
        FillOperation.REPLACE)
    blocks.fill(WATER, pos(-8, -1, -8), pos(8, -1, 8), FillOperation.OUTLINE)
player.on_item_interacted(KELP_ITEM, on_item_interacted_kelp)

def on_item_interacted_trident():
    for value in animals:
        for index4 in range(4):
            mobs.spawn(value, randpos(pos(-4, 10, -4), pos(4, 10, 4)))
player.on_item_interacted(TRIDENT, on_item_interacted_trident)

def on_item_interacted_apple():
    global size, spiral
    size = 3
    spiral = 20
    builder.teleport_to(player.position())
    builder.mark()
    for index5 in range(spiral):
        builder.move(FORWARD, size)
        builder.move(UP, 1)
        builder.turn(LEFT_TURN)
        builder.trace_path(CHERRY_LEAVES)
    builder.move(FORWARD, 1)
    builder.move(LEFT, 1)
    builder.mark()
    builder.move(FORWARD, size - 2)
    builder.move(LEFT, size - 2)
    builder.move(DOWN, spiral)
    builder.fill(CHERRY_LOG)
player.on_item_interacted(APPLE, on_item_interacted_apple)

def on_item_interacted_blaze_rod():
    shapes.circle(MAGMA_BLOCK,
        pos(0, -1, 0),
        5,
        Axis.Y,
        ShapeOperation.OUTLINE)
    shapes.circle(FIRE, pos(0, 0, 0), 5, Axis.Y, ShapeOperation.OUTLINE)
player.on_item_interacted(BLAZE_ROD, on_item_interacted_blaze_rod)

spiral = 0
size = 0
animals: List[number] = []
animals = [DOLPHIN, SEA_TURTLE, SALMON, TROPICAL_FISH]