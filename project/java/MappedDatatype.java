package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public class MappedDatatype  {

  private ExtensionInline extension;
  private String standard;
  private Boolean builtin;
  private String pattern;
  private String element;
  private Integer size;
  private String parameter;
  private String minInclusive;
  private String maxInclusive;
  private Annotation annotation;
  private String base;


}