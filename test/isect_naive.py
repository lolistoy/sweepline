from typing import List, Optional, Tuple
from sweepline import Segment, Point, ZERO


def point_on_seg(pt: Point, seg: Segment):
    if not (min(seg.start.x, seg.end.x) <= pt.x <= max(seg.start.x, seg.end.x)):
        return False
    if not (min(seg.start.y, seg.end.y) <= pt.y <= max(seg.start.y, seg.end.y)):
        return False
    v1 = pt - seg.start
    v2 = pt - seg.end
    return (v1.x * v2.y - v2.x * v1.y) == ZERO


def isect_segmens_naive(segs: List, include_endpoints: bool = False) -> List:
    n = len(segs)
    seg_objs = [Segment(Point(*seg[0]), Point(*seg[1])) for seg in segs]
    results = []
    for i in range(n):
        segi = seg_objs[i]
        for j in range(i + 1, n):
            segj = seg_objs[j]
            if include_endpoints:
                if point_on_seg(segi.start, segj):
                    results.append(segi.start)
                if point_on_seg(segi.end, segj):
                    results.append(segi.end)
                if point_on_seg(segj.start, segi):
                    results.append(segj.start)
                if point_on_seg(segj.end, segi):
                    results.append(segj.end)
            res = segi.isect(segj)
            if res and res != segi.start and res != segi.end and res != segj.start and res != segj.end:
                results.append(res)

    results = list(set(results))

    return [(float(res.x), float(res.y)) for res in results]
