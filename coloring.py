# Color arrows
def color(arrows):
    colors_used = 0
    left_arrows_rj = larj = {}
    right_arrows_rj = rarj = {}
    coloring = {}

    arrows.sort()
    for ai in arrows:
        colors = []
        for c in range(1, colors_used+1):
            if ai[0] < ai[1]:
                if rarj[c] < ai[0] and larj[c] < ai[1]:
                    colors.append(c)
            if ai[1] < ai[0]:
                if rarj[c] < ai[1] and larj[c] < ai[1]:
                    colors.append(c)

        if colors != []:
            rjs = [max(larj[c], rarj[c]) for c in colors]
            color_for_ai = cfai = colors[rjs.index(max(rjs))]
            coloring[ai] = cfai

            if ai[0] < ai[1] and rarj[cfai] < ai[1]:
                rarj[cfai] = ai[1]
            if ai[1] < ai[0] and larj[cfai] < ai[0]:
                larj[cfai] = ai[0]
        else:
            colors_used += 1
            coloring[ai] = colors_used
            if ai[0] < ai[1]:
                rarj[colors_used] = ai[1]
                larj[colors_used] = -1
            if ai[1] < ai[0]:
                larj[colors_used] = ai[0]
                rarj[colors_used] = -1
    return colors_used

if __name__ == '__main__':
    arrows = [(3,10), (1,5), (14,11), (9,12), (8,4)]
    colors = color(arrows)
    print('Colors used: ' + str(colors))
    # print('colors_used: '+ str(colors_used) + '\n')
    # print('arrows: ' + str(arrows) + '\n')
    # print('larj: ' + str(larj) + '\n')
    # print('rarj: ' + str(rarj) + '\n')
