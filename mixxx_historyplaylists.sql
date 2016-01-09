/*  SQL requests for getting historical playlists out of Mixxx
    sqlite3 mixxxdb.sqlite      */


/* Tracks for specific playlist */

select 
p.name, pt.position, tl.filename, tl.location 
from 
Playlists as p, PlaylistTracks as pt, track_locations as tl 
where 
pt.playlist_id = 40     /* Change here */
and p.id=pt.playlist_id 
and pt.track_id = tl.id 
order by pt.position;

/* All tracks from all history playlists in their original order */

select 
p.name, pt.position, tl.filename, tl.location 
from Playlists p
join PlaylistTracks pt on pt.playlist_id = p.id 
join track_locations tl on pt.track_id = tl.id
order by p.name, pt.position;
