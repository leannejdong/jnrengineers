player.onItemInteracted(SNOWBALL, function on_item_interacted_snowball() {
    blocks.fill(SNOW, pos(-10, -1, -10), pos(10, -1, 10), FillOperation.Replace)
    for (let index = 0; index < 50; index++) {
        mobs.spawn(SNOWBALL_PROJECTILE_MOB, randpos(pos(-10, 10, -10), pos(10, 10, 10)))
    }
})
player.onChat("sand", function on_on_chat() {
    for (let index2 = 0; index2 < 100; index2++) {
        blocks.place(SAND, randpos(pos(-10, 10, -10), pos(10, 10, 10)))
        blocks.place(ORANGE_CONCRETE_POWDER, randpos(pos(-10, 10, -10), pos(10, 10, 10)))
    }
})
player.onItemInteracted(IRON_AXE, function on_item_interacted_iron_axe() {
    for (let index3 = 0; index3 < 20; index3++) {
        mobs.spawn(LIGHTNING_BOLT, randpos(posCamera(-5, 0, 5), posCamera(5, 0, 10)))
    }
})
player.onItemInteracted(KELP_ITEM, function on_item_interacted_kelp() {
    blocks.fill(SEA_LANTERN, positions.groundPosition(pos(-10, 0, -10)), positions.groundPosition(pos(10, 0, 10)), FillOperation.Replace)
    blocks.fill(AIR, positions.groundPosition(pos(-9, 0, -9)), positions.groundPosition(pos(9, 0, 9)), FillOperation.Replace)
    blocks.fill(WATER, pos(-8, -1, -8), pos(8, -1, 8), FillOperation.Outline)
})
player.onItemInteracted(TRIDENT, function on_item_interacted_trident() {
    for (let value of animals) {
        for (let index4 = 0; index4 < 4; index4++) {
            mobs.spawn(value, randpos(pos(-4, 10, -4), pos(4, 10, 4)))
        }
    }
})
player.onItemInteracted(APPLE, function on_item_interacted_apple() {
    
    size = 3
    spiral = 20
    builder.teleportTo(player.position())
    builder.mark()
    for (let index5 = 0; index5 < spiral; index5++) {
        builder.move(FORWARD, size)
        builder.move(UP, 1)
        builder.turn(LEFT_TURN)
        builder.tracePath(CHERRY_LEAVES)
    }
    builder.move(FORWARD, 1)
    builder.move(LEFT, 1)
    builder.mark()
    builder.move(FORWARD, size - 2)
    builder.move(LEFT, size - 2)
    builder.move(DOWN, spiral)
    builder.fill(CHERRY_LOG)
})
player.onItemInteracted(BLAZE_ROD, function on_item_interacted_blaze_rod() {
    shapes.circle(MAGMA_BLOCK, pos(0, -1, 0), 5, Axis.Y, ShapeOperation.Outline)
    shapes.circle(FIRE, pos(0, 0, 0), 5, Axis.Y, ShapeOperation.Outline)
})
let spiral = 0
let size = 0
let animals : number[] = []
animals = [DOLPHIN, SEA_TURTLE, SALMON, TROPICAL_FISH]
