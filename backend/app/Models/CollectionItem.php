<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class CollectionItem extends Model
{
    protected $table = 'collection_items';
    public $timestamps = false;
    protected $fillable = ['collection_id','artifact_id','note','added_at'];
    public function collection() { return $this->belongsTo(Collection::class); }
    public function artifact() { return $this->belongsTo(Artifact::class); }
}
