<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Artifact extends Model
{
    protected $table = 'artifacts';
    const UPDATED_AT = null;
    protected $fillable = ['museum_id','name','era','material','dimensions','description_vi','description_en','image_urls','source_note'];
    protected $casts = ['image_urls' => 'array'];

    public function museum() { return $this->belongsTo(Museum::class); }
    public function hotspots() { return $this->hasMany(Hotspot::class); }
    public function collectionItems() { return $this->hasMany(CollectionItem::class); }
}
